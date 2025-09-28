import numpy as np
import pandas as pd

# #Series
# se1=pd.Series(np.random.randint(1,100,10))
# print('se1:\n',se1)
# print('se1.array:\n',se1.array)
# print('se1.index:\n',se1.index)
# se2=pd.Series(range(7),index=list('abcdefg'))
# print('se2:\n',se2)
# print('se2.index:\n',se2.index)
# print('se2.array:\n',se2.array)
# print('se2[se2>3]:\n',se2[se2>3])
# print('np.exp(se2):\n',np.exp(se2))
# #Series像字典，可以用字典创建Series对象
# sdata = {"Ohio": 35000, "Texas": 71000, "Oregon": 16000, "Utah": 5000}
# se3=pd.Series(sdata)
# print('se3:\n',se3)
# #用to_dict方法转换为字典
# print('se2.to_dict()=',se2.to_dict())
# #可主动设置索引的位置.没有"California"找到 的值，它显示为NaN(Not a Number)，这在 Pandas 中被视为缺失值或NA值。由于"Utah"不包含在 中states，因此它被排除在结果对象之外。
# states = ["California", "Ohio", "Oregon", "Texas"]
# se4=pd.Series(sdata,index=states)
# print('se4:\n',se4)
# #检查是否有缺失值
# print('pd.isna(se4):\n',pd.isna(se4))
# print('pd.notna(se4)\n',pd.notna(se4))
# #算术运算中自动按索引标签对齐：
# print('se3+se4:\n',se3+se4)
# #Series 对象本身及其索引都具有一个name属性
# se4.name='population'
# se4.index.name='state'
# print('se4:\n',se4)
##如果索引包含整数，s[]的数据选择将始终以标签为导向，而不是位置

# #Dataframe 可以被认为是一个包含所有共享相同索引的 Series 的字典，一列相当于一个Series对象
# #用字典创建Dataframe
# data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
#         "year": [2000, 2001, 2002, 2001, 2002, 2003],
#         "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
# df1 = pd.DataFrame(data)
# print('df1\n',df1)
# #指定列的顺序
# df2=pd.DataFrame(data,columns=['year','state','pop','debt'])
# print('df2:\n',df2)
# print('df2[\'state\']:\n',df2['state'])
# #用赋值修改列
# df2['debt']=np.random.randint(1,200,6)
# print('df2:\n',df2)
# #讲Series对象赋值给Dataframe，自动对齐标签
# val=pd.Series([-1.2, -1.5, -1.7], index=[2, 4, 5])
# df2['debt']=val
# print('df2:\n',df2)
# df2["eastern"] =df2["state"] == "Ohio"
# print('df2:\n',df2)
# #删除列
# del df2["eastern"]
# print('df2:\n',df2)
# #字典的嵌套字典创建Dataframe,pandas 会将外部字典键解释为列，将内部键解释为行索引
# populations = {"Ohio": {2000: 1.5, 2001: 1.7, 2002: 3.6},"Nevada": {2001: 2.4, 2002: 2.9}}
# df3=pd.DataFrame(populations)
# print('df3:\n',df3)
# #转置
# print('df3.T:\n',df3.T)
# df3.index=[2010,2011,2012]
# df3.columns=['aaa','bbb']
# print('df3:\n',df3)
# df4=pd.DataFrame([2,3,4,5,6])
# print('df4:\n',df4)

#iloc\loc
df1=pd.DataFrame(np.random.randint(0,10,(5,4)),index=['a','b','c','d','e'],columns=['one','two','three','four'])
print('df1:\n',df1)
#print(df1[0:2,0:2])错误
#print(df1[0])#错误，没有索引为0的列
print(df1[0:1])#只能用切片或iloc
print('df1[\'one\']:\n',df1['one'])
print('df1[df1[\'one\']>3]:\n',df1[df1['one']>3])
print('df1[0:2]:\n',df1[0:2])
print('df1.loc[\'a\':\'c\',\'one\':\'three\']:\n',df1.loc['a':'c','one':'three'])#包含
df1[df1<5]=0
print(df1)

# data2 = pd.DataFrame(np.arange(16).reshape((4, 4)),index=["Ohio", "Colorado", "Utah", "New York"],columns=["one", "two", "three", "four"])
# print(data2)
# print(data2.three)
# print(data2[0:2])#注意，[]是可以放入行切片的，但不能切片列
# print(data2.iloc[0:2,0:2])
# print(data2["three"] > 5)
# print(data2[data2["three"] > 5])#注意，[]是可以放入行切片的，所以带上了第0、1、3列
# print(data2[data2.three > 5])
# print(data2.loc[data2.three > 5])#loc只能传入一维数组