Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import seaborn as sns
>>> tips = sns.load_dataset("tips")
>>> tips.head()
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
>>> g = sns.lmplot(x='total_bill', y='tip',data=tips)
>>> import matplotlib.pyplot as plt
>>> plt.show()
>>> g = sns.lmplot(x='total_bill', y='tip',data=tips,hue='smoker')
>>> plt.show()
>>> g = sns.lmplot(x='total_bill', y='tip',data=tips,hue='smoker',palette='Set1')
>>> plt.show()
>>> g = sns.lmplot(x='total_bill', y='tip',data=tips,col='smoker',palette='Set1')
>>> plt.show()
>>> 
