# imporrt libraries
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 

data = pd.read_csv('Penguins Data.csv')

# check for null values
data.info()
print(data.isnull().sum())

# visualising the null values
plt.figure(figsize=(12,8))
sns.heatmap(data.isnull(), cbar=False, cmap="crest")
plt.show()

# handling the null values
df = data.dropna(thresh=10)   

print(df.info())
print(df.isnull().sum())

# handle numerical nulls
num_cols = ['Culmen Length (mm)', 'Culmen Depth (mm)', 
            'Flipper Length (mm)', 'Body Mass (g)']

df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

# handle categorical null values
df = df.fillna('unknown')

# making a heat map for checking the correlations
num_df = df.select_dtypes(include=['number'])

corr = num_df.corr()
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='BrBG', fmt=".2f")

plt.title("Correlation Heatmap")
plt.show()

df[num_cols].plot(
    kind='box',
    subplots=True,
    layout=(3, 2),
    sharey=False
)

plt.tight_layout()
plt.show()

# making a count plot for gender
sns.countplot(x='Gender', data=df)
plt.show()