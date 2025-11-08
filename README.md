# Analytics_Agent_for_Healthcare_Data

Transforming structured healthcare data into actionable insights using natural language queries with LLMs.

## Overview
This Python project allows healthcare analysts, data scientists, and AI-interested doctors to interact with patient datasets using natural language. Powered by Llama3 (local), it can quickly generate pandas queries to extract insights from your Excel files—no long waits for manual data exploration.
The system is especially useful for healthcare analytics, enabling fast analysis of patient demographics, billing, doctor performance, and departmental statistics.

## Features
•  Automatically generates pandas code from natural language questions using a local Llama3 model.
•  Executes generated code safely and displays results in tabular format.
•  Provides data context including column info, sample rows, and summary statistics.
•  Ideal for healthcare analytics to analyze patient datasets such as revenue, demographics, and departmental statistics.
•  Handles both DataFrame and Series results, ensuring seamless tabular display.
• Can also be connected to DB instead of expected Excel dataset in sheets (patient_data.xlsx).

## Use Case
Designed for healthcare analytics, it enables doctors, analysts, or researchers to:
•	Quickly answer questions like:
o	"Show all patients from the Gastrology department"
o	"What's the total Net Amount by Department?"
o	"Show patients with Net Amount greater than 500"
o	"How many patients per doctor?"
o	"What's the average age by Gender?"
o	"Show all male patients from UK"
•	Avoid waiting for manual queries and data aggregation.

## Installation & Dependencies
Ensure you have Python ≥ 3.10 and the following dependencies:
pip install pandas==2.5.3
pip install tabulate==0.9.0
pip install ollama==0.1.0
pip install openpyxl  # For Excel file support
Note: Versions are indicative. Adjust as per your environment.
•	Ollama must be installed and running locally (ollama serve) to use the LLM model.

## Usage
1.	Run the main script: python analytics.py
2.	Enter your Excel file path (default: patient_data.xlsx).
3.	Enter natural language questions about the dataset.
4.	Results are displayed in tabular format.

## Author

**Dr. Akshaya Tharankini A**  
Healthcare Data & AI Specialist | SQL | Python | Power BI  
*Email: drakshayatharankini@gmail.com*  
*LinkedIn: https://www.linkedin.com/in/dr-akshaya-tharankini/*
