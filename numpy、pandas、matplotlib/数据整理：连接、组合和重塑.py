import numpy as np
import pandas as pd
import matplotlib基础语法.pyplot as plt


# #Series的分层索引
# data = pd.Series(np.random.uniform(size=9),index=[["a", "a", "a", "b", "b", "c", "c", "d", "d"],[1, 2, 3, 1, 3, 1, 2, 2, 3]])
# print('data:\n',data,sep="")
# #注意，这是Series，不是Dataframe
# print('data[[\'a\',\'b\']]:\n',data[['a','b']],sep="")
# #第二个参数是第二层引用
# print('data.loc[:,2]:\n',data.loc[:,2],sep="")
# #Series转变到Dataframe中
# print('data.unstack():\n',data.unstack(),sep="")

# #Dataframe的分层索引
# frame = pd.DataFrame(np.arange(12).reshape((4, 3)),index=[["a", "a", "b", "b"], [1, 2, 1, 2]],columns=[["Ohio", "Ohio", "Colorado"],["Green", "Red", "Green"]])
# print('frame:\n',frame,sep="")
# frame.index.names = ["key1", "key2"]
# frame.columns.names = ["state", "color"]
# print('frame:\n',frame,sep="")
# print('frame["Ohio"]:\n',frame["Ohio"],sep="\n")
# #换索引位置
# print('frame.swaplevel("key1", "key2"):\n',frame.swaplevel("key1", "key2"),sep="")
# print('frame.sort_index():\n',frame.sort_index(),sep="")
# print('frame.sort_index(level=1):\n',frame.sort_index(level=1),sep="")
# #按级别汇总统计
# print('frame.groupby(level="key2"):\n',frame.groupby(level="key2"),sep="")
# print('frame.groupby(level="key2").sum():\n',frame.groupby(level="key2").sum(),sep="")
# print('frame.T.groupby(level="color").sum().T:\n',frame.T.groupby(level="color").sum().T,sep="")

# #使用 DataFrame 的列进行索引
# frame = pd.DataFrame({"a": range(7), "b": range(7, 0, -1),"c": ["one", "one", "one", "two", "two","two", "two"],"d": [0, 1, 2, 0, 1, 2, 3]})
# print('frame;\n', frame,sep="")
# frame2=frame.set_index(["c", "d"])
# print('frame2;\n', frame2,sep="")
# #默认情况下，列将从 DataFrame 中删除，但您可以通过传递drop=False给以下方式保留它们set_index：
# print('frame.set_index(["c", "d"], drop=False):\n', frame.set_index(["c", "d"], drop=False))
# #逆操作
# print('frame2.reset_index():\n', frame2.reset_index())

# #索引合并
# right1 = pd.DataFrame({"key": ["a", "b", "a", "a", "b", "c"],"value": pd.Series(range(6), dtype="Int64")})
# left1 = pd.DataFrame({"group_val": [3.5, 7]}, index=["a", "b"])
# print(pd.merge(left1, right1, left_index=True, right_on="key"))

#用Dataframe创建Dataframe
data1 = pd.DataFrame(np.arange(6).reshape((2, 3)), index=pd.Index(["Ohio", "Colorado"], name="state"), columns=pd.Index(["one", "two", "three"], name="number"))
print('data1:\n', data1,sep="")
data2=pd.DataFrame(data1)
print('data2:\n', data2,sep="")
#当在 DataFrame 中取消堆叠时，取消堆叠的级别将成为结果中的最低级别：
result = data1.stack()
df = pd.DataFrame({"left": result, "right": result + 5},columns=pd.Index(["left", "right"], name="side"))
print('df:\n', df,sep="")
print('df.unstack(level="state"):\n', df.unstack(level="state"), sep="")
#与 一样unstack，调用时stack我们可以指示要堆叠的轴的名称：
print('df.unstack(level="state").stack(level="side"):\n', df.unstack(level="state").stack(level="side"), sep="")
