# **Analytics Agent for Healthcare Data**
Transform structured healthcare data into actionable insights — using natural language queries with LLMs.

---

## **Overview**
This Python project allows healthcare analysts, data scientists, and AI-interested doctors to query patient datasets using natural language.

Powered by Llama3 (local) — it generates pandas code automatically to extract insights from Excel files, eliminating slow manual data exploration.

Use cases include:
- patient demographics
- billing & revenue analysis
- doctor performance
- departmental statistics

## **Features**
- Generates pandas code from natural language questions (local Llama3 model)
- Executes queries safely and displays results in tabular format
- Provides data context (columns, sample rows, summary statistics)
- Designed for healthcare analytics use cases (revenue, demographics, department KPIs)
- Handles DataFrame & Series results seamlessly
- Can connect to database (not only Excel)

## **Example Questions**
- “Show all patients from the Gastrology department”
- “What’s the total Net Amount by Department?”
- “Show patients with Net Amount > 500”
- “How many patients per doctor?”
- “What’s the average age by Gender?”
- “Show all male patients from UK”

## **Installation & Dependencies**
Requires Python 3.10+
bash
pip install pandas==2.5.3
pip install tabulate==0.9.0
pip install ollama==0.1.0
pip install openpyxl     

## **Usage** 
1.	Run the main script: python analytics.py
2.	Enter your Excel file path (default: patient_data.xlsx).
3.	Enter natural language questions about the dataset.
4.	Results are displayed in tabular format.

## Author

**Dr. Akshaya Tharankini A**  
Healthcare Data & AI Specialist | SQL | Python | Power BI  
*Email: drakshayatharankini@gmail.com*  
*LinkedIn: https://www.linkedin.com/in/dr-akshaya-tharankini/*
