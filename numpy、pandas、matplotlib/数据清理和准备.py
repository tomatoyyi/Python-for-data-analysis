import numpy as np
import pandas as pd

# data1 = pd.DataFrame([[1., 6.5, 3.], [1., np.nan, np.nan],[np.nan, np.nan, np.nan], [np.nan, 6.5, 3.]])
# print(data1)
# print(data1.isna())
# print(data1[data1>3])
# data1[data1>3]=100#[]可放入同形状布尔数组
# print(data1[data1.isna()])
# print(data1.loc[[0,1,0,1]])

# data1 = pd.DataFrame([[1., 6.5, 3.], [1., np.nan, np.nan],[np.nan, np.nan, np.nan], [np.nan, 6.5, 3.]])
# print(data1)
# #删除有非数字的行
# print('data1.dropna(axis=0,how=\'any\'):\n',data1.dropna(axis=0,how='any'))
# #删除全是非数字的行
# print('data1.dropna(axis=0,how=\'all\'):\n',data1.dropna(axis=0,how='all'))
# #指定每行 / 列至少需要保留的非 NaN 值的数量，只有满足这个数量要求的行 / 列才会被保留下来。
# print('data1.dropna(axis=0,thresh=1):\n',data1.dropna(axis=0,thresh=1))
# #可用fillna指定缺失值替代
# print('data1.fillna(0):\n',data1.fillna(0))
# #用字典指定某一列用什么填充
# print('data1.fillna({0:100,1:200,2:300}):\n',data1.fillna({0:100,1:200,2:300}))
# #fillna的参数还可以是ffill、data.mean()平均值等

# data3 = pd.DataFrame({"k1": ["one", "two"] * 3 + ["two"],"k2": [1, 1, 2, 3, 3, 4, 4]})
# print('data3:\n',data3)
# #duplicated返回一个布尔系列，指示每一行是否重复（其列值与前一行中的列值完全相等）
# print('data3.duplicated():\n',data3.duplicated())
# print('data3.drop_duplicates()\n',data3.drop_duplicates())
# #直接加一行
# data3['v2']=range(7)
# print('data3:\n',data3)
# #只想通过某列筛选重复项,last参数保留最后一个
# print('data3.drop_duplicates(subset=[\'k1\']):\n',data3.drop_duplicates(subset=['k1']))
# print('data3.drop_duplicates(["k1", "k2"], keep="last"):\n',data3.drop_duplicates(["k1", "k2"],keep="last"))

# #使用函数或映射转换数据
# data = pd.DataFrame({"food": ["bacon", "pulled pork", "bacon", "pastrami", "corned beef", "bacon","pastrami", "honey ham", "nova lox"],"ounces": [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
# print('data:\n',data)
# meat_to_animal = {
#   "bacon": "pig",
#   "pulled pork": "pig",
#   "pastrami": "cow",
#   "corned beef": "cow",
#   "honey ham": "pig",
#   "nova lox": "salmon"
# }
# #用map建立映射
# data["animal"] = data["food"].map(meat_to_animal)
# print('data:\n',data)
#
# def get_animal(x):
#   return meat_to_animal[x]
# print(data["food"].map(get_animal))#传入的函数以food列的值作为参数

# #重命名轴索引
# data = pd.DataFrame(np.arange(12).reshape((3, 4)),index=["Ohio", "Colorado", "New York"],columns=["one", "two", "three", "four"])
# print(data)
# def transform(x):
#   return x[:4].upper()
#
# print(data.index.map(transform))
# data.index=data.index.map(transform)
# print(data)
# #不改变源数据
# print(data.rename(index={"OHIO": "INDIANA"},columns={"three": "peekaboo"}))

# #离散化和分箱，例如年龄分段
# ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
# bins = [18, 25, 35, 60, 100]
# age_categories_num = pd.cut(ages, bins)
# print('age_categories:\n', age_categories_num)
# print('age_categories.value_counts():\n', age_categories_num.value_counts())
# group_names = ["Youth", "YoungAdult", "MiddleAged", "Senior"]
# age_categories_label=pd.cut(ages, bins, labels=group_names)
# print('age_categories_label:\n', age_categories_label)
# #如果传递整数，将根据数据中的最小值和最大值计算等长区间
# data1 = np.random.uniform(size=20)
# age_categories_length=pd.cut(data1,4,precision=2)
# print('age_categories_length:\n', age_categories_length)
##qcut通过样本分位分箱，每个区间有相同数量。如分为四份，则为0~25%，25~50%，50~75%，75~100%，也可以手动传分位

# df1=pd.DataFrame(np.random.randint(0,5,(5,4)),index=['a','b','c','d','e'],columns=['one','two','three','four'])
# print('df1:\n',df1)
# print(df1.agg(pd.value_counts, dropna=False).fillna(0))


#检测和过滤异常值
data=pd.DataFrame(np.random.standard_normal((1000,4)))
print(data.describe())
#找第一列绝对值超过3的值的行
col=data[0]
print('abs>3:\n',col[col.abs()>3])
#用布尔数组筛选行，只保留 True 对应的行，即 “至少有一列绝对值>3” 的行。.any结果是一个一维布尔数组（长度等于行数）
print('data[(data.abs() > 3).any(axis="columns")]:\n',data[(data.abs() > 3).any(axis="columns")])