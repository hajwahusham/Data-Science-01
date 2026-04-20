# load basic libraries
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 
import warnings
warnings.filterwarnings('ignore')

# reading the csv file
df = pd.read_csv("heart.csv")

# display the first few rows
df.head()

# display the dataset shape
df.shape

# display columnn names
df.columns

# display descriptive statistics
df.describe()

# check for null values
df.isnull().sum()

# display dataset information
print(df.info())

# create histogram
df.hist(figsize=(12, 12), layout=(5, 3))
plt.show()

# create box and whiskers plots
df.plot(kind='box', subplots=True, layout=(5, 3), figsize=(12,12))
plt.show()

# create barplot
sns.barplot(data=df, x='sex', y='chol', hue='target', palette='spring')
plt.show()

# display value counts for sex column
df['sex']. value_counts()

# display value counts for target column
df['target'].value_counts()

# display value counts for thal column
df['thal'].value_counts()

# create correlation heatmap
plt.figure(figsize=(20, 10))
sns.heatmap(df.corr(), annot=True, cmap='terrain')
plt.show()

# create countplot for sex vs target
sns.countplot(x='sex', data=df, palette='husl', hue='target')
plt.show()

# create countplot for target
sns.countplot(x= 'target', palette='BuGn', data=df)
plt.show()

# create countplot for ca vs target
sns.countplot(x='ca', hue='target', data=df)
plt.show()