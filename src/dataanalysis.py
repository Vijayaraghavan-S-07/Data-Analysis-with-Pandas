import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('dataanalysis.csv')

# Display the first few rows of the data
print(df.head())

# Describe the data and get descriptive statistics for all numerical columns
print(df.describe())

# Find missing values in each column
mval = df.isnull().sum()
print("Missing values in each column:\n", mval)

# Calculate the average of the 'Age' column
ave = df['Age'].mean()
print(f"Average of age: {ave}")

# Count the unique values in the 'Age' column
un_age = df['Age'].nunique()
print(f"Unique ages: {un_age}")

# Find the highest-paid employee
hp_emp = df.loc[df['Salary'].idxmax()]
print(f"Highest paid employee:\n{hp_emp}")

# Count the number of employees in each department
emp_dept = df['Department'].value_counts()
print("Number of employees in each department:\n", emp_dept)

# Count employees by gender
gender_count = df['Gender'].value_counts()
print("Number of employees by gender:\n", gender_count)

# Sort employees by seniority (assuming 'Age' is a proxy for seniority)
sor_emp = df.sort_values(by='Age', ascending=False)
print("Employees sorted from senior to junior:\n", sor_emp.head())

# Plot: Distribution of Salaries
plt.figure(figsize=(8, 5))
plt.hist(df['Salary'], bins=10, color='skyblue', edgecolor='black')
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

# Plot: Number of employees in each department
plt.figure(figsize=(8, 5))
emp_dept.plot(kind='bar', color='orange')
plt.title('Employees per Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)
plt.show()

# Plot: Gender distribution
plt.figure(figsize=(8, 5))
gender_count.plot(kind='pie', autopct='%1.1f%%', colors=['lightblue', 'pink'], labels=gender_count.index)
plt.title('Gender Distribution')
plt.ylabel('')  # Remove y-axis label for clarity
plt.show()

# Plot: Age vs Salary scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(df['Age'], df['Salary'], color='green', alpha=0.7)
plt.title('Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()