# importing packages
import seaborn
import matplotlib.pyplot as plt 

########## main section ########
# loading dataset using seaborn
df = seaborn.load_dataset('tips')
# pair plot with hue sex
seaborn.pairplot(df, hue= 'sex')
# to show
plt.show()