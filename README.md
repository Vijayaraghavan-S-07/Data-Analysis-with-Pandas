# Data-Analysis-with-Pandas

This task demonstrates how to perform basic data analysis tasks using the Pandas library. The analysis includes reading a CSV file, performing descriptive statistics, handling missing values, calculating averages, and more.

# Features
Load CSV Data: Read data from a CSV file using Pandas.
Explore Data: Display the first few rows of the dataset for initial inspection.
Descriptive Statistics: Generate statistical summaries (mean, count, min, max, etc.) for numerical columns.
Missing Data: Identify and count missing values in each column.
Basic Calculations:
  Calculate averages for specific columns.
  Count unique values in a column.
  Identify the highest-paid employee.
  Count the number of employees in each department.
  Rank employees from senior to junior (based on age).

# How It Works
This tool performs the following operations:

1. Load Data:
  Load data from a CSV file into a Pandas DataFrame.

2. Display Data:
  Display the first few rows of the dataset using df.head().
  
3. Descriptive Statistics:
  Use df.describe() to generate a summary of statistics for all numerical columns.

4. Missing Values:
  Check for missing values in each column using df.isnull().sum().

5. Basic Calculations:
  Average: Compute the average (mean) of the Age column using df['Age'].mean().
  Unique Values: Count the unique values in the Age column using df['Age'].nunique().
  Additional Analysis:
    Highest Paid Employee: Identify the employee with the highest salary using df.loc[df['Salary'].idxmax()].
    Number of Employees in Each Department: Use df['Department'].value_counts() to count employees in each department.
    Rank Employees (Senior to Junior): Sort employees by age to rank from senior (oldest) to junior (youngest) using df.sort_values(by='Age', ascending=False).
   
7. Data Visualization:
  Plot graphs (e.g., salary distribution or employee count per department) using Matplotlib.
