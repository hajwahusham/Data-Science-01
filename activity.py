import numpy as np
import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as sns 

# read data from csv file
df = pd.read_csv("country_vaccinations.csv")

# display the first 10 rows
df.head(10)

# check for any null values in each column
df.isnull().any()

# visualize missing values using a heatmap (optimize by using a subset of data)
subset = df.iloc[:5200, :]
plt.figure(figsize=(12,8))
sns.heatmap(subset.isnull(), cbar=False, cmap="viridis")

# display the fist 10 rows
df.head(10)

# drop rows where all values are NaN
df.dropna(how="all")

# fill missing values using backward fill method
df.bfill()

# interpolate missing values


# drop all rows with any NaN values
df_dropped = df.dropna()
df_dropped