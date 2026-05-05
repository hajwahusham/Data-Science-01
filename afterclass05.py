# imporrt libraries
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 
import warnings
warnings.filterwarnings('ignore')

# reading the csv file
df = pd.read_csv("Penguins Data.csv")

# make a scatter plot between features culmen length and body mass
plt.scatter(x=df['Culmen Length (mm)'], y=df['Body Mass (g)'], 
            c="pink",
            linewidths= 1,
            marker= "D",
            edgecolors= "teal",
            s= 50)

plt.xlabel("Culmen Length (mm)")
plt.ylabel("Body Mass (g)")
plt.show()

# make a scatter plot between features culmen depth and body mass
plt.scatter(x=df['Culmen Depth (mm)'], y=df['Body Mass (g)'], 
            c="tab:olive",
            linewidths= 1,
            marker= "D",
            edgecolors= "teal",
            s= 50)

plt.xlabel("Culmen Depth (mm)")
plt.ylabel("Body Mass (g)")
plt.show()

# make a pair plot between features culmen length and body mass
sns.pairplot(df, hue='Species', palette='Dark2')
plt.show()

# make an area graph between features culmen length and body mass
df_sorted = df.sort_values('Culmen Length (mm)')

x = df_sorted['Culmen Length (mm)']
y = df_sorted['Body Mass (g)']

plt.plot(x, y, color="tab:blue")
plt.fill_between(x, y, alpha=0.3, color="tab:blue")

plt.xlabel("Culmen Length (mm)")
plt.ylabel("Body Mass (g)")
plt.title("Area Graph: Culmen Length vs Body Mass")

plt.show()