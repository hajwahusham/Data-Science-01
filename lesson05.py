# importing libraries
import pandas as pd  
import numpy as np  
import seaborn as sns 
import matplotlib.pyplot as plt 

# load dataset
housedf = pd.read_csv("USA_Housing (1).csv")

# display the first few rows
housedf.head()

# display dataset information
housedf.info()

# display column names
housedf.columns

# create pairplot
sns.pairplot(housedf)

# create heatmap of correlations
sns.heatmap(housedf.corr(), annot=True)