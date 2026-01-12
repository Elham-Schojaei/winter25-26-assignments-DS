# Part 1: Reading and inspecting data:

import pandas as pd

url = "https://raw.githubusercontent.com/TechLabs-Dusseldorf/winter25-26-assignments-DS/73681664066b345c7d239a9af038212d74800609/global_sales.csv"

df = pd.read_csv(url)

#print(df.head())

# Print the first 5 rows
print(df.head(5))

# Print data types of all columns
print(df.dtypes)



# Part 2: Data Cleaning and Indexing:

# Calculate the mean of Units_Sold
mean_units_Sold = df["Units_Sold"].mean()
print("\nMean of Units_Sold:", mean_units_Sold)

# Fill missing values with the mean
df["Units_Sold"] = df["Units_Sold"].fillna(mean_units_Sold)
#fillna():Replace missing values (NaN) with something else.
print("\nUnits_Sold: \n" ,df["Units_Sold"])



df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
#pd.to_numeric() is a pandas function that converts data to a numeric type (like int or float).
#errors="coerce" means: if pandas sees something non-numeric, it will turn it into NaN.

df["Sales"] = df["Sales"].fillna(0).astype(float)
#astype() : Convert a column (or DataFrame) to a different data type.

print("\nSales: \n" ,df["Sales"])



print("\nDate_type: \n", df["Date"].dtypes)
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
print("\nNew_Date_type: \n", df["Date"].dtypes)



#set_index() :To set OrderID as the new index 
df = df.set_index("OrderID")
print(df.head())

#Reset the index (OrderID goes back to a normal column)
df = df.reset_index()
print("\n", df.head())

#Set Date as the index
df = df.set_index("Date")
print("\n",df.head())

#Sort by date for time series work
df = df.sort_index()
print("\n",df.head())



# Part 3: Filtering, Modifying, and Sorting

high_value_sales = df.loc[(df["Sales"] > 500) & (df["Region"] == "Europe")]
print("\nhigh_value_sale: \n", high_value_sales.head())


df.loc[5, "Units_Sold"] = 99
print("\nModified Units_Sold at index 5: \n", df.loc[5])


df["Profit"] = df["Sales"] * 0.20
print("\nDataFrame with Profit column: \n", df.head())


df_sorted = df.sort_values( by=["Region", "Sales"], ascending=[True, False])

print("\ndf_sorted\n", df_sorted.head())



# Part 4: Grouping and Aggregation (Analysis)

# 1. Regional Performance:

# Step 1: group by Region
grouped = df.groupby("Region", as_index=False)
print("\ngrouped:\n", grouped)
#grouped = df.groupby(...) → creates a GroupBy object (not visible like a table)

# Step 2: aggregate (sum Sales, mean Units_Sold)
regional_performance = grouped.agg(Total_Sales=("Sales", "sum"), Avg_Units_Sold=("Units_Sold", "mean"))
print("\nregional_performance:\n", regional_performance)


# anothe example
Product_performance = (
    df.groupby("Product", as_index=False)
      .agg(
          Total_Sales=("Sales", "sum"),
          Avg_Units_Sold=("Units_Sold", "mean")
      )
)

print("\nProduct_performance:\n", Product_performance)



#2. Product Deep Dive:

# Step 1: group by Product
grouped = df.groupby("Product", as_index=False)

# Step 2: select the Profit column from the grouped object
grouped_profit = grouped["Profit"]
print("\ngrouped_profit:\n", grouped_profit)

# Step 3: take the maximum Profit in each product group
max_profit = grouped_profit.max()
print("\nmax_profit:\n", max_profit)

# Step 4: rename the Profit column to Max_Profit
max_profit_by_product = max_profit.rename(columns={"Profit": "Max_Profit"})

# Step 5: print the result
print("\nmax_profit_by_product:\n", max_profit_by_product)



