# import pandas and matplotlib
import pandas as pd  
import matplotlib.pyplot as plt 
import numpy as np 

# creating a dataframe with birth rate data of july
br_july = {
    "day":['mon', 'tue', 
           'wed', 'thu', 'fri', 
           'sat', 'sun'],
    "new births": [12,15,11,9,1,9,21]
} 

july_df = pd.DataFrame(br_july)

# plot a bar graph and customise
plt.figure(figsize=(8, 4))
plt.bar(br_july['day'], br_july['new births'], width=0.6, color="#00B7A7")
plt.xlabel('day')
plt.ylabel('new births')
plt.title('birth rate data of july')
plt.xticks(rotation=45)
# zip joins x and y coordinates in pairs
for x,y in zip(br_july['day'], br_july['new births']):
    label = f"({y})".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # this is the point label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
    
plt.show()

# creating a dataframe with birthrate data of august
br_aug = {
    "day":['mon', 'tue', 
           'wed', 'thu', 'fri', 
           'sat', 'sun'],
    "new births": [17,5,2,11,1,8,29]
} 

aug_df = pd.DataFrame(br_aug)

# plot a bar graph and customise
plt.figure(figsize=(8, 4))
plt.bar(br_aug['day'], br_aug['new births'], width=0.6, color="#DC1655")
plt.xlabel('day')
plt.ylabel('new births')
plt.title('birth rate data of august')
plt.xticks(rotation=45)
# zip joins x and y coordinates in pairs
for x,y in zip(br_aug['day'], br_aug['new births']):
    label = f"({y})".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # this is the point label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
    
plt.show()

# compare by plotting on the same graph
july_df_new = july_df.rename(columns={'new births': 'july'})
aug_df_new = aug_df.rename(columns={'new births': 'august'})
df_merged = july_df_new.merge(aug_df_new, on='day')
print(df_merged)

x = np.arange(len(df_merged['day']))
plt.figure(figsize=(8, 4))
plt.bar(x - 0.2, df_merged['july'], width=0.4, label='july', color="#00B7A7")
plt.bar(x + 0.2, df_merged['august'], width=0.4, label='august', color="#DC1655")

plt.xticks(x, df_merged['day'])
plt.xlabel("day")
plt.ylabel("new births")
plt.title("july vs. august: birth rate")
plt.legend()
plt.show()