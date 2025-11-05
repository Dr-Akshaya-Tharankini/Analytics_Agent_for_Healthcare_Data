import pandas as pd
import json
from ollama import chat
from tabulate import tabulate
import os

class AnalyticsChat:
    def __init__(self, excel_file):
        """Initialize with Excel file path"""
        self.model = "llama3:latest"
        self.df = self.load_excel_data(excel_file)
        
    def load_excel_data(self, file_path):
        """Load data from Excel file"""
        try:
            df = pd.read_excel(file_path)
            print(f" Loaded {len(df)} rows from {file_path}")
            print(f" Columns: {', '.join(df.columns)}\n")
            return df
        except Exception as e:
            print(f" Error loading Excel file: {str(e)}")
            return None
    
    def get_data_context(self):
        """Generate context about the data"""
        if self.df is None:
            return "No data loaded"
        
        context = f"""Dataset Information:
Table Name: patient_data
Total Rows: {len(self.df)}
Columns: {', '.join(self.df.columns)}

Column Details:
{self.df.dtypes.to_string()}

Sample Data (first 3 rows):
{self.df.head(3).to_string()}

Summary Statistics:
{self.df.describe(include='all').to_string()}
"""
        return context
    
    def generate_query(self, user_question):
        """Use Llama3 to generate pandas query from natural language"""
        data_context = self.get_data_context()
        
        prompt = f"""You are a data analyst assistant. Given the following dataset and a user question, generate Python pandas code to answer the question.

{data_context}

User Question: {user_question}

Generate ONLY the Python code needed to answer this question. The code should:
1. Use the variable 'df' which contains the patient data DataFrame
2. Store the result in a variable called 'result'
3. Result should be a pandas DataFrame or Series that can be displayed as a table
4. Use proper pandas methods for filtering, grouping, aggregating, etc.

IMPORTANT: Return ONLY the Python code, no explanations, no markdown formatting, no backticks.

Example format:
result = df.groupby('Department')['Net Amount'].sum().reset_index()

Code:"""

        try:
            response = chat(
                model=self.model,
                messages=[{
                    'role': 'user',
                    'content': prompt
                }],
                options={
                    'temperature': 0.1,
                    'num_predict': 300
                }
            )
            
            code = response['message']['content'].strip()
            # Clean up code if it has markdown formatting
            code = code.replace('```python', '').replace('```', '').strip()
            # Remove any leading/trailing quotes
            code = code.strip('"\'')
            
            return code
        except Exception as e:
            print(f" Error calling Ollama: {str(e)}")
            print("Make sure Ollama is running: ollama serve")
            return None
    
    def execute_query(self, code):
        """Safely execute the generated code"""
        try:
            local_vars = {'df': self.df, 'pd': pd}
            exec(code, {"__builtins__": {}}, local_vars)
            result = local_vars.get('result')
            
            if result is None:
                return None, "No result generated"
            
            # Convert to DataFrame if it's a Series
            if isinstance(result, pd.Series):
                result = result.to_frame().reset_index()
            
            return result, None
        except Exception as e:
            return None, f"Error executing query: {str(e)}"
    
    def chat(self, user_question):
        """Main chat function"""
        if self.df is None:
            print("No data loaded. Please check the Excel file.")
            return None
            
        print(f"\n Question: {user_question}\n")
        print("Generating query with Llama3...")
        
        # Generate code using LLM
        code = self.generate_query(user_question)
        
        if code is None:
            return None
            
        print(f"Generated code:\n{code}\n")
        
        # Execute the code
        result, error = self.execute_query(code)
        
        if error:
            print(f" {error}")
            return None
        
        # Display results in tabular form
        print(" Results:\n")
        print(tabulate(result, headers='keys', tablefmt='grid', showindex=False))
        print(f"\n Found {len(result)} rows")
        
        return result


def main():
    """Main function to run the analytics chat"""
    print("=" * 70)
    print(" ANALYTICS CHAT DEMO - Powered by Llama3 (Local)")
    print("=" * 70)
    
    # Get Excel file path
    excel_file = input("\n Enter Excel file path (or press Enter for 'patient_data.xlsx'): ").strip()
    if not excel_file:
        excel_file = "patient_data.xlsx"
    
    if not os.path.exists(excel_file):
        print(f" File not found: {excel_file}")
        print("Please provide a valid Excel file path.")
        return
    
    # Initialize chat
    chat_bot = AnalyticsChat(excel_file)
    
    if chat_bot.df is None:
        return
    
    print("\n" + "=" * 70)
    print("Example questions you can ask:")
    print("  • Show me all patients from Plastic Surgery department")
    print("  • What's the total Net Amount by Department?")
    print("  • Show patients with Net Amount greater than 500")
    print("  • How many patients per doctor?")
    print("  • What's the average age by Gender?")
    print("  • Show me all Male patients from Yemen")
    print("\nType 'quit' to exit")
    print("=" * 70)
    
    while True:
        try:
            question = input("\n Ask a question: ").strip()
            
            if question.lower() in ['quit', 'exit', 'q']:
                print("\n Goodbye!")
                break
            
            if not question:
                continue
            
            chat_bot.chat(question)
            
        except KeyboardInterrupt:
            print("\n\n Goodbye!")
            break
        except Exception as e:
            print(f" Error: {str(e)}")


if __name__ == "__main__":
    main()