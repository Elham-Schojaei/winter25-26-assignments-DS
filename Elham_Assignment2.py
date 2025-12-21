# Assignment 2: E-commerce Inventory Analyst

## Part 1: NumPy Array Manipulation (The Core Data)

# 1. Product Data:

import numpy as np
product_ids = np.arange(1000, 1050,5)
print("Product IDs:", product_ids)


stock = np.arange(20, 120, 10)
sales = np.random.uniform(1.0, 25.0, size=10)
sales = np.round(sales, 1)
cost = np.random.uniform(5.0, 50.0, size=10)
cost = np.round(cost, 2)

stock = stock.reshape(10, 1)
sales = sales.reshape(10, 1)
cost  = cost.reshape(10, 1)

print("stock:\n", stock)
print("sales:\n", sales)
print("cost:\n", cost)

inventory_data = np.concatenate((stock, sales, cost), axis=1)
print("Inventory Data:\n", inventory_data)


# 2. Basic Calculations and Attributes:

print(inventory_data.shape)
print(inventory_data.dtype)

stock = inventory_data[:, 0]
cost  = inventory_data[:, 2]
total_value = stock * cost
print("Total Value of the current stock for all products:\n", total_value)


 #3. Slicing, Indexing, and Statistics:

print("products 3 through 7: \n" ,inventory_data[3:8])

print("Average Weekly Sales: \n" ,np.mean(inventory_data[:,1]))

print("Unit Cost of the product at index 0: \n",inventory_data[0, 2])


## Part 2: Advanced NumPy Analysis (Re-stocking Logic)

# 1. Boolean Masking (The "Low-Stock" Check):

weeks_of_stock = inventory_data[:, 0] / inventory_data[:, 1]
print("weeks_of_stock: \n" , weeks_of_stock)


mask = weeks_of_stock < 4
print("Weeks of Stock is less than 4: \n ", mask)

print("the entire rows for the products that are low in stock: \n",inventory_data [mask])


#2. Reshaping and Concatenation (Updating Data):

reorder_quantity = 4*inventory_data[:,1] - inventory_data[:,0] 
print("Reorder Quantity: \n", reorder_quantity)

for i in range(len(reorder_quantity)):
    if reorder_quantity[i] < 0:
        reorder_quantity[i] = 0

print("Reorder Quantity after adjustment: \n", reorder_quantity)


reorder_quantity = reorder_quantity.reshape(10,1)
print("Reorder Quantity reshaped: \n", reorder_quantity)

updated_inventory_data = np.concatenate((inventory_data, reorder_quantity), axis=1)
print("Updated Inventory Data with Reorder Quantity: \n", updated_inventory_data)

## Part 3: Introduction to Pandas (Viewing the Results)

#  1. Create a DataFrame:

import pandas as pd

df_inventory_data = pd.DataFrame(updated_inventory_data, columns=[ "Current Stock", "Avg Weekly Sales", "Unit Cost", "Reorder Quantity"])

print ("Pandas DataFrame: \n",df_inventory_data)


#2. Basic Selection:

Current_Stock_coloumn = df_inventory_data["Current Stock"]
print("Current Stock Column:\n", Current_Stock_coloumn)

Reorder_Quantity_coloumn = df_inventory_data["Reorder Quantity"]
print("Reorder Quantity Column:\n", Reorder_Quantity_coloumn)   

df_inventory_data_first_rows = df_inventory_data.head(5)
print("First 5 rows of the DataFrame:\n", df_inventory_data_first_rows)
