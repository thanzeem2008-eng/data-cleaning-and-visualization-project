# 📊 Forbes Global 2000 - Data Cleaning & Visualization

## 📌 Project Overview

This project focuses on **data cleaning, preprocessing, outlier detection, and visualization** using the Forbes Global 2000 dataset.

The main goal is to transform raw company data into a clean and meaningful dataset and create visualizations that help understand company performance based on **Sales, Profits, Assets, and Market Value**.

---

## 🎯 Objectives

- Clean and preprocess the raw dataset
- Handle missing values
- Remove duplicate records
- Detect outliers using the IQR method
- Convert financial values into numerical format
- Analyze company performance
- Create meaningful visualizations
- Build a single dashboard containing multiple graphs
- Extract useful insights from the dataset

---

## 🛠️ Technologies Used

- 🐍 Python
- 🐼 Pandas
- 📊 Matplotlib
- 📈 Seaborn
- 📗 Excel

---

## 📂 Dataset

The dataset contains information about **Forbes Global 2000 companies**, including:

| Column | Description |
|--------|-------------|
| Rank | Company's ranking |
| Company | Company name |
| Country | Country of the company |
| Sales | Company sales |
| Profits | Company profits |
| Assets | Company assets |
| MarketValue | Company market value |

---

## 🧹 Data Cleaning Process

The following preprocessing steps were performed:

1. Loaded the Excel dataset using Pandas.
2. Removed unnecessary/empty rows.
3. Renamed columns for easier analysis.
4. Cleaned company and country names.
5. Converted Rank into numerical format.
6. Converted financial values into numerical values.
7. Identified missing values.
8. Filled missing numerical values using the median.
9. Filled missing text values with `Unknown`.
10. Checked and removed duplicate records.
11. Detected outliers using the **Interquartile Range (IQR)** method.

---

## 📊 Visualizations

The project contains a single dashboard with the following visualizations:

### 1. Distribution of Financial Features
Shows the distribution of Sales, Profits, Assets, and Market Value.

### 2. Top 10 Companies by Sales
Shows the companies with the highest sales.

### 3. Top 10 Companies by Profits
Shows the companies with the highest profits.

### 4. Top 10 Companies by Market Value
Shows companies with the highest market value.

### 5. Top 10 Countries by Number of Companies
Shows which countries have the largest number of companies in the dataset.

### 6. Sales vs Profits
A scatter plot showing the relationship between company sales and profits.

### 7. Correlation Heatmap
Shows the correlation between numerical features.

### 8. Box Plot
Helps visualize the spread of financial values and identify potential outliers.

### 9. Assets vs Market Value
Shows the relationship between company assets and market value.

---

## 📈 Key Insights

The analysis identifies:

- 🏆 Company with the highest sales
- 💰 Company with the highest profits
- 📈 Company with the highest market value
- 🌍 Country with the highest number of companies
- 📊 Average sales
- 💵 Average profits
- 🔎 Relationships between financial features

---

## 📁 Project Files

```text
Forbes-Data-Analysis/
│
├── ForbesGlobal20002014.xlsx
│
├── data_science_task1.py
│
├── Forbes_Global_2000_Cleaned.xlsx
│
├── Forbes_Data_Analysis_Dashboard.png
│
└── README.md
