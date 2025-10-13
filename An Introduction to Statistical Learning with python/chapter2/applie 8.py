import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
college=pd.read_csv("college.csv")
print('college.head():\n',college.head())
college2 = pd.read_csv('College.csv', index_col=0)
college = college.rename({'Unnamed: 0': 'College'},axis=1)
college = college.set_index('College')
print('college.head()重索引:\n',college.head())
print('college.describe():\n',college.describe())
# #散点图矩阵
# pd.plotting.scatter_matrix(college[['Top10perc', 'Apps', 'Enroll']])
# #箱型图
# college.boxplot('Outstate',by='Private')
college['Ellite']=pd.cut(college['Top10perc'],[0,50,100],labels=['No', 'Yes'])
print('college精英判断:\n',college.head(15))
print(college['Ellite'].value_counts())
plt.show()
