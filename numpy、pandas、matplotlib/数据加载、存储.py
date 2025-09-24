import numpy as np
import pandas as pd
import sys
import json

#csv
# data1=pd.DataFrame(np.random.randint(0,10,(5,4)),index=['a','b','c','d','e'],columns=['one','two','three','four'])
# data1.index.name='index'
# print('data1:\n',data1)
# data1.to_csv('exa_data.csv')
# data2=pd.read_csv('exa_data.csv',index_col='index')
# print('data2:\n',data2,)

# #json
# #data=pd.read_json('exa_json.json')
# dict1={'name': 'Wes',
#  'cities_lived': ['Akron', 'Nashville', 'New York', 'San Francisco'],
#  'pet': None,
#  'siblings': [{'name': 'Scott',
#    'age': 34,
#    'hobbies': ['guitars', 'soccer']},
#   {'name': 'Katie', 'age': 42, 'hobbies': ['diving', 'art']}]}
# print('dict1:',dict1)
# asjson1=json.dumps(dict1)
# print('asjson1:',asjson1)


#excel
#Excelfile读取
xlsx1=pd.ExcelFile('ema_xlsx1.xlsx')
print(xlsx1.sheet_names)
print('xlsx1:\n',xlsx1.parse(sheet_name='Sheet1', index_col=0))
#read_excel读取
xlsx2=pd.read_excel('ema_xlsx2.xlsx',sheet_name='Sheet1',index_col=0)
random_df=pd.DataFrame(np.random.randint(-100,100,size=xlsx2.shape),columns=xlsx2.columns,index=xlsx2.index)
xlsx2 = xlsx2.where(~xlsx2.isna(),random_df)#注意，跟numpy 的whre不一样
xlsx2.index.name='numbers'
xlsx2.columns.name='characters'
print(xlsx2)
xlsx2.to_excel('ema_xlsx3.xlsx')
xlsx3=pd.read_excel('ema_xlsx3.xlsx',index_col='numbers')
print(xlsx3)