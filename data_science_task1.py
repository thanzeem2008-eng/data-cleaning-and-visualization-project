# ==========================================
# FORBES GLOBAL 2000 - DATA CLEANING &
# VISUALIZATION PROJECT
# ==========================================

# ==========================================
# 1. IMPORT LIBRARIES
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ==========================================
# 2. LOAD DATASET
# ==========================================

file_path = "ForbesGlobal20002014.xlsx"

# Skip the first empty row
df = pd.read_excel(
    file_path,
    skiprows=1
)

print("Original Dataset:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)


# ==========================================
# 3. RENAME COLUMNS
# ==========================================

df.columns = [
    "Rank",
    "Company",
    "Country",
    "Sales",
    "Profits",
    "Assets",
    "MarketValue"
]

print("\nColumn Names:")
print(df.columns)


# ==========================================
# 4. REMOVE EMPTY ROWS
# ==========================================

df.dropna(
    how="all",
    inplace=True
)


# ==========================================
# 5. REMOVE EXTRA HEADER ROW
# ==========================================

# The Excel file contains one extra row:
# Rank | Company | Country | Sales | Profits | Assets | Market

df = df[
    df["Company"].astype(str).str.strip().str.lower()
    != "company"
]


# ==========================================
# 6. CLEAN TEXT COLUMNS
# ==========================================

df["Company"] = (
    df["Company"]
    .astype(str)
    .str.strip()
)

df["Country"] = (
    df["Country"]
    .astype(str)
    .str.strip()
)


# ==========================================
# 7. CONVERT RANK TO NUMERIC
# ==========================================

df["Rank"] = pd.to_numeric(
    df["Rank"],
    errors="coerce"
)


# ==========================================
# 8. FUNCTION TO CONVERT MONEY VALUES
# ==========================================

def convert_money(value):

    if pd.isna(value):
        return None

    value = str(value)

    # Remove dollar symbol
    value = value.replace("$", "")

    # Remove normal spaces
    value = value.replace(" ", "")

    # Remove non-breaking spaces
    value = value.replace("\xa0", "")

    # Convert comma decimal to dot
    value = value.replace(",", ".")

    # Remove B and M symbols
    value = value.replace("B", "")
    value = value.replace("M", "")

    try:
        return float(value)

    except:
        return None


# ==========================================
# 9. CONVERT FINANCIAL COLUMNS
# ==========================================

financial_columns = [
    "Sales",
    "Profits",
    "Assets",
    "MarketValue"
]

for column in financial_columns:

    df[column] = df[column].apply(
        convert_money
    )


# ==========================================
# 10. CHECK MISSING VALUES
# ==========================================

print("\n==========================================")
print("MISSING VALUES BEFORE CLEANING")
print("==========================================")

print(
    df.isnull().sum()
)


# ==========================================
# 11. HANDLE MISSING VALUES
# ==========================================

numeric_columns = [
    "Rank",
    "Sales",
    "Profits",
    "Assets",
    "MarketValue"
]

# Fill numerical missing values with median
for column in numeric_columns:

    if df[column].notna().any():

        df[column] = df[column].fillna(
            df[column].median()
        )


# Fill missing text values
df["Company"] = df["Company"].replace(
    "nan",
    "Unknown"
)

df["Country"] = df["Country"].replace(
    "nan",
    "Unknown"
)

df["Company"] = df["Company"].fillna(
    "Unknown"
)

df["Country"] = df["Country"].fillna(
    "Unknown"
)


# ==========================================
# 12. REMOVE DUPLICATES
# ==========================================

duplicate_count = df.duplicated().sum()

print("\nNumber of duplicate rows:")
print(duplicate_count)

df.drop_duplicates(
    inplace=True
)


# ==========================================
# 13. OUTLIER DETECTION USING IQR
# ==========================================

print("\n==========================================")
print("OUTLIER DETECTION")
print("==========================================")

for column in financial_columns:

    Q1 = df[column].quantile(0.25)

    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR

    upper_limit = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_limit)
        |
        (df[column] > upper_limit)
    ]

    print(
        column,
        "Outliers:",
        len(outliers)
    )


# ==========================================
# 14. DISPLAY CLEANED DATA
# ==========================================

print("\n==========================================")
print("CLEANED DATA")
print("==========================================")

print(
    df.head()
)

print(
    "\nDataset Shape After Cleaning:"
)

print(
    df.shape
)

print(
    "\nData Types:"
)

print(
    df.dtypes
)


# ==========================================
# 15. SAVE CLEANED DATASET
# ==========================================

output_file = (
    "Forbes_Global_2000_Cleaned.xlsx"
)

df.to_excel(
    output_file,
    index=False
)

print(
    "\nCleaned dataset saved as:",
    output_file
)


# ==========================================
# 16. CREATE DASHBOARD
# ==========================================

fig, axes = plt.subplots(
    3,
    3,
    figsize=(20, 16)
)


# ==========================================
# GRAPH 1 - DISTRIBUTION
# ==========================================

for column in financial_columns:

    axes[0, 0].hist(
        df[column].dropna(),
        bins=20,
        alpha=0.5,
        label=column
    )

axes[0, 0].set_title(
    "Distribution of Financial Features"
)

axes[0, 0].set_xlabel(
    "Value"
)

axes[0, 0].set_ylabel(
    "Frequency"
)

axes[0, 0].legend()


# ==========================================
# GRAPH 2 - TOP 10 SALES
# ==========================================

top_sales = df.sort_values(
    "Sales",
    ascending=False
).head(10)

axes[0, 1].bar(
    top_sales["Company"],
    top_sales["Sales"]
)

axes[0, 1].set_title(
    "Top 10 Companies by Sales"
)

axes[0, 1].set_xlabel(
    "Company"
)

axes[0, 1].set_ylabel(
    "Sales"
)

axes[0, 1].tick_params(
    axis="x",
    rotation=45
)


# ==========================================
# GRAPH 3 - TOP 10 PROFITS
# ==========================================

top_profits = df.sort_values(
    "Profits",
    ascending=False
).head(10)

axes[0, 2].bar(
    top_profits["Company"],
    top_profits["Profits"]
)

axes[0, 2].set_title(
    "Top 10 Companies by Profits"
)

axes[0, 2].set_xlabel(
    "Company"
)

axes[0, 2].set_ylabel(
    "Profits"
)

axes[0, 2].tick_params(
    axis="x",
    rotation=45
)


# ==========================================
# GRAPH 4 - TOP 10 MARKET VALUE
# ==========================================

top_market = df.sort_values(
    "MarketValue",
    ascending=False
).head(10)

axes[1, 0].bar(
    top_market["Company"],
    top_market["MarketValue"]
)

axes[1, 0].set_title(
    "Top 10 Companies by Market Value"
)

axes[1, 0].set_xlabel(
    "Company"
)

axes[1, 0].set_ylabel(
    "Market Value"
)

axes[1, 0].tick_params(
    axis="x",
    rotation=45
)


# ==========================================
# GRAPH 5 - TOP COUNTRIES
# ==========================================

country_counts = (
    df["Country"]
    .value_counts()
    .head(10)
)

axes[1, 1].bar(
    country_counts.index,
    country_counts.values
)

axes[1, 1].set_title(
    "Top 10 Countries by Number of Companies"
)

axes[1, 1].set_xlabel(
    "Country"
)

axes[1, 1].set_ylabel(
    "Number of Companies"
)

axes[1, 1].tick_params(
    axis="x",
    rotation=45
)


# ==========================================
# GRAPH 6 - SALES VS PROFITS
# ==========================================

axes[1, 2].scatter(
    df["Sales"],
    df["Profits"],
    alpha=0.6
)

axes[1, 2].set_title(
    "Sales vs Profits"
)

axes[1, 2].set_xlabel(
    "Sales"
)

axes[1, 2].set_ylabel(
    "Profits"
)


# ==========================================
# GRAPH 7 - CORRELATION HEATMAP
# ==========================================

correlation = (
    df[numeric_columns]
    .corr()
)

sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    ax=axes[2, 0]
)

axes[2, 0].set_title(
    "Correlation Heatmap"
)


# ==========================================
# GRAPH 8 - BOX PLOT
# ==========================================

sns.boxplot(
    data=df[financial_columns],
    ax=axes[2, 1]
)

axes[2, 1].set_title(
    "Box Plot of Financial Features"
)

axes[2, 1].set_xlabel(
    "Financial Feature"
)

axes[2, 1].set_ylabel(
    "Value"
)

axes[2, 1].tick_params(
    axis="x",
    rotation=45
)


# ==========================================
# GRAPH 9 - ASSETS VS MARKET VALUE
# ==========================================

axes[2, 2].scatter(
    df["Assets"],
    df["MarketValue"],
    alpha=0.6
)

axes[2, 2].set_title(
    "Assets vs Market Value"
)

axes[2, 2].set_xlabel(
    "Assets"
)

axes[2, 2].set_ylabel(
    "Market Value"
)


# ==========================================
# DASHBOARD TITLE
# ==========================================

fig.suptitle(
    "Forbes Global 2000 - Data Analysis Dashboard",
    fontsize=20,
    fontweight="bold"
)


# ==========================================
# IMPROVE SPACING
# ==========================================

plt.subplots_adjust(
    left=0.05,
    right=0.98,
    top=0.93,
    bottom=0.07,
    wspace=0.30,
    hspace=0.45
)


# ==========================================
# SAVE DASHBOARD
# ==========================================

dashboard_file = (
    "Forbes_Data_Analysis_Dashboard.png"
)

plt.savefig(
    dashboard_file,
    dpi=300,
    bbox_inches="tight"
)

print(
    "\nDashboard saved as:",
    dashboard_file
)


# ==========================================
# SHOW DASHBOARD
# ==========================================

plt.show()


# ==========================================
# 17. KEY INSIGHTS
# ==========================================

print("\n==========================================")
print("KEY INSIGHTS")
print("==========================================")


# Highest Sales
highest_sales = df.loc[
    df["Sales"].idxmax()
]

print(
    "\nHighest Sales Company:",
    highest_sales["Company"]
)

print(
    "Sales:",
    highest_sales["Sales"]
)


# Highest Profits
highest_profits = df.loc[
    df["Profits"].idxmax()
]

print(
    "\nHighest Profits Company:",
    highest_profits["Company"]
)

print(
    "Profits:",
    highest_profits["Profits"]
)


# Highest Market Value
highest_market = df.loc[
    df["MarketValue"].idxmax()
]

print(
    "\nHighest Market Value Company:",
    highest_market["Company"]
)

print(
    "Market Value:",
    highest_market["MarketValue"]
)


# Country with most companies
top_country = (
    df["Country"]
    .value_counts()
    .idxmax()
)

top_country_count = (
    df["Country"]
    .value_counts()
    .max()
)

print(
    "\nCountry with Most Companies:",
    top_country
)

print(
    "Number of Companies:",
    top_country_count
)


# Total companies
print(
    "\nTotal Companies:",
    len(df)
)


# Average Sales
print(
    "\nAverage Sales:",
    round(
        df["Sales"].mean(),
        2
    )
)


# Average Profits
print(
    "Average Profits:",
    round(
        df["Profits"].mean(),
        2
    )
)


# ==========================================
# PROJECT COMPLETED
# ==========================================

print("\n==========================================")
print("PROJECT COMPLETED SUCCESSFULLY!")
print("==========================================")
