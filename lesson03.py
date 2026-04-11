# import pandas and matplotlib
import pandas as pd  
import matplotlib.pyplot as plt  

# upload file to make a copy of the file
countries_df = pd.read_csv('Countries.csv')
countries = countries_df
countries.head(3)

# extract the rows where the year is 1952
c_52 = countries.loc[countries['year']==1952]
c_52.head()

# extract the rows where the year is 2007
c_07 = countries.loc[countries['year']==2007]
c_07.head()

type(c_52)

# merge the '52 and  '07 dataframes together
c_merge = c_52.merge(c_07, left_on='country', right_on='country')
c_merge.head()

# drop both the year columns
c_merge.drop(['year_x', 'year_y'], axis=1)
c_merge.head

# create a new column that takes the difference between population_y and the population_x column
c_merge['population_growth'] = c_merge['population_y'] - c_merge['population_x']
c_merge.head()

# test the math
31889923 - 8425333

c_merge.shape, type(c_merge)

# sort the values so you get back the 10 countries with the biggest population
c_merge = c_merge.sort_values('population_growth', ascending=False).head(10)
c_merge.head(10)

# plotting the data
names = ['China', 'India', 'United States', 'Indonesia', 'Brazil', 'Pakistan', 'Bangladesh', 'Nigeria', 'Mexico', 'Philippines']
pop_grow = (c_merge['population_growth'] / 10**6)

plt.figure(figsize=(15,9))
plt.bar(names, pop_grow, width=0.6)
plt.xlabel('Country')
plt.ylabel('Population Growth (Millions)')
plt.title('top 10 countries with the biggest population growth from 1952 to 2007')
plt.xticks(rotation=45)

# zip joins x and y coordinates in pairs
for x,y in zip(names,pop_grow):
    label = "({:.2f})".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # this is the point label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
    
plt.show()