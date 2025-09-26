import numpy as np
import pandas as pd

df = pd.DataFrame({"key1" : ["a", "a", None, "b", "b", "a", None],"key2" : pd.Series([1, 2, 1, 2, 1, None, 1],dtype="Int64"),"data1" : np.random.standard_normal(7),"data2" : np.random.standard_normal(7)})
print('df:\n',df,sep="")
grouped=df['data1'].groupby(df['key1'])
print('grouped:\n',grouped,sep="")
print('grouped.mean():\n',grouped.mean(),sep="")
#除了组键，有非数字的列时要注意，用numeric_only=True
print('df.groupby("key2").mean(numeric_only=True):\n',df.groupby("key2").mean(numeric_only=True),sep="")

#数据聚合
print('df:\n',df,sep="")
grouped=df.groupby(df["key1"])
print('grouped:\n',grouped,sep="")
#roupBy 没有明确实现该方法，但我们仍然可以将其与未优化的实现一起使用。GroupBy 内部会将 Series 切片，piece.nsmallest(n)对每个切片调用相应的方法
print('grouped["data1"].nsmallest(2):\n',grouped["data1"].nsmallest(2),sep="")