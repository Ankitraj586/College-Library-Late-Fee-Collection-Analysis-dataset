# College-Library-Late-Fee-Collection-Analysis-dataset

##  Project Overview

This project analyzes **college library late fee data** using Python.  
The goal is to understand how late book returns affect the **fine amount** and how fines vary across **different departments**.
The project uses **data analysis and visualization** to find useful insights.

## Objectives

- Analyze late book return days
- Study fine amount charged to students
- Compare fine data across departments
- Visualize patterns using graphs
- Understand relationship between late days and fine amount

## Dataset Information
The dataset is a CSV file with **1000 records**.

### Columns in the dataset:
- Student_ID – Unique ID of student
- Book_ID – Book identification number
- Department – Student department (CE, CSE, IT, etc.)
- Issue_Date – Date when book was issued
- Due_Date – Last return date
- Return_Date – Actual return date
- Late_Days – Number of days book was returned late
- Fine_Amount – Fine charged in rupees

##  Tools & Libraries Used

1. **Python**
 2. **NumPy** – Numerical calculations
 3. **Pandas** – Data handling and analysis
 4. **Matplotlib** – Data visualization
 5. **Seaborn** – Statistical plots

##  Data Cleaning
Before analysis, the dataset was checked:
- No missing values
- No duplicate records
- Correct data types
- Only required columns were selected for analysis

## Exploratory Data Analysis (EDA)
### Statistical Summary:
- Average Late Days= 12 days
- Average Fine Amount= ₹60
- Maximum Fine= ₹120
- Minimum Fine=₹0
This shows that higher late days result in higher fines.

### Department-wise Analysis
- Fine records were counted for each department
- Some departments have more late return cases than others
This helps library management identify problem areas.

### Data Visualization
The following plots were created
1. **Histogram of Departments**  
  Shows distribution of students across departments

 2. **Histogram of Late Days**  
  Shows how late students return books

3. **Boxplot (Department vs Fine Amount)**  
  Compares fine amount across departments  
  Shows minimum, maximum, median, and outliers

> Graphs make the data easy to understand.


### Key Findings

- Late days and fine amount are directly related
- Some departments show higher fine cases
- Fine system works in a structured manner
- Visualization helps in better decision making
