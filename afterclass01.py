import numpy as np
import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as sns 

# read data from csv file
df = pd.read_csv("detective mk's log.csv", encoding="cp1252")

# display the first 10 rows
new = df.head(10)
print(new)
print("-------------------------next-------------------------")

# check for any null values in each column
new = df.isnull().any()
print(new)
print("-------------------------next-------------------------")


# visualize missing values using a heatmap (optimize by using a subset of data)
subset = df.iloc[:5200, :]
plt.figure(figsize=(12,8))
sns.heatmap(subset.isnull(), cbar=False, cmap="viridis")
plt.show()

# drop rows where all values are NaN
new = df.dropna(how="all")
print(new)
print("-------------------------next-------------------------")


# fill missing values using backward fill method
new = df.bfill()
print(new)
print("-------------------------next-------------------------")


# drop all rows with any NaN values
df_dropped = df.dropna()
print(df_dropped)
print("-------------------------end-------------------------")
