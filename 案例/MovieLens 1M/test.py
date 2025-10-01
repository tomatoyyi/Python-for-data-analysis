import pandas as pd
import numpy as np

data = {'Alice': [165], 'Bob': [180], 'Charlie': [170]}
s1 = pd.DataFrame(data).T
s1.columns=['sg']
print("原始数据:")
print(s1)
s1['pm'] = s1['sg'].argsort()
print("s1['sg'].argsort():\n",s1['sg'].argsort(),sep="")
print("s1.sort_values(by='sg', ascending=False):\n",s1.sort_values(by='sg', ascending=False),sep="")

s=pd.DataFrame(np.random.standard_normal(size=(10,4)),columns=['A','B','C','D'])
s['A_argsort'] = s['A'].argsort()
print('对Aargsort数据：\n',s,sep="")
print('对A排序数组：\n',s.sort_values(by='A'))