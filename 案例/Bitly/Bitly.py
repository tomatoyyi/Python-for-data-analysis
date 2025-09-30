import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 显示所有列
pd.set_option('display.max_columns', None)
path = r"Bitly\bitly_usagov\example.txt"

with open(path,encoding='utf-8') as f:
    records = [json.loads(line) for line in f]


#时区对比
#print(records[0])#字典太难看
#print(json.dumps(records[0], ensure_ascii=False, indent=4))#用json格式查看便于观察
frame=pd.DataFrame(records)
#print(frame.head())
time_zone=frame['tz'].fillna("MISSING")
time_zone[time_zone==""]="UNKNOWN"
time_zone=time_zone.value_counts()#注意.value_counts()是对单列数据
print('time_zone:\n',time_zone,sep="")
#分析时区分布
#matplolib分析时区
subset=time_zone.head(5)
fig3,ax3=plt.subplots(figsize=(16, 9))
# 自动生成颜色，根据柱子数量生成不同的颜色
# np.linspace(0, 1, len(subset)) 生成在 0 到 1 之间、数量与柱子数相同的均匀分布数，用于取色
colors = plt.cm.viridis(np.linspace(0, 1, len(subset)))
ax3.barh(subset.index,subset.values,height=0.6,color=colors)
ax3.set_title('top_5_tz', fontsize=16)
ax3.set_ylabel('counts', fontsize=12)
ax3.set_xlabel('time_zone', fontsize=12)
for i,value in enumerate(subset.values):
    ax3.text(value+20,i,str(value),ha='center', va='bottom')
ax3.grid(axis='y', linestyle='--', alpha=0.7)
#用seaborn分析时区
subset=time_zone.head()
fig0,ax0=plt.subplots(figsize=(16, 9))
sns.barplot(y=subset.index, x=subset.values,hue=subset.index,palette='magma',ax=ax0)
for i,value in enumerate(subset.values):
    ax0.text(value+20,i,str(value),ha='center', va='bottom')



#分析windows分布
# # 完全不限制列宽
pd.set_option('display.width', 1000)  # 根据实际情况调整宽度值
pd.set_option('display.max_columns', None)  # 显示所有列
pd.set_option('display.max_colwidth', None)#控制dataframe的列宽
pd.set_option('display.colheader_justify', 'left')#display.colheader_justify 只控制列名的对齐方式，而数据内容默认就是左对齐的。如果你发现某些列右对齐，可能是因为它们是数值类型，可以用 df.style 来单独调整。
print("frame[['a']][0:30].style.set_properties(**{'text-align': 'left'}:\n",frame[['a']][0:30].style.set_properties(**{'text-align': 'left'},sep="").to_string())
#print(frame['a'].value_counts().reset_index().head(25))#reset_index()可以让series数据变成dataframe
print("frame['a'].value_counts().head(25):\n",frame['a'].value_counts().head(25),sep="")


#只看是否是windows
cframe=frame[frame['a'].notna()].copy()#排除掉没有标识的行
cframe['os']=np.where(cframe["a"].str.contains("Windows"),"Windows", "Not Windows")
print('cframe[\'os\'].head():\n',cframe['os'].head(),sep="")
by_tz_os = cframe.groupby(["tz", "os"])
print('by_tz_os.head()(groupby未聚合前):\n',by_tz_os.head(),sep="")
#当你在 GroupBy 对象上调用一个聚合函数时，Pandas 才会真正执行分组和计算。在这个阶段，为了清晰地展示结果，Pandas 会将你用于分组的列（tz 和 os）自动设置为结果的多级索引（MultiIndex）。
#用.size才能计算出每一组的数量，给缺失值填充0方便之后计算
agg_counts = by_tz_os.size().unstack().fillna(0)
print('agg_counts:\n',agg_counts,sep="")
#找出设备数最多的10个地方
indexer=agg_counts.sum('columns').argsort()
count_subset=agg_counts.take(indexer[-10:])
count_subset.rename(index={"":'UNKNOWN'},inplace=True)
print('count_subset:\n',count_subset,sep="")

fig, axes = plt.subplots(2, 1, figsize=(16, 9))

#用seaborn画图
#要变成长格式才能识别,注意melt之前要先reset_index
count_subset=count_subset.reset_index()
print('re_count_subset:\n',count_subset,sep="")
long_count_subset=pd.melt(count_subset,id_vars='tz',value_vars=['Not Windows','Windows'])
print('long_c_s.head(10):\n',long_count_subset.head(30),sep="")
sns.barplot(x='value',y='tz',hue='os',data=long_count_subset,ax=axes[0])
axes[0].set_title("Number of Windows users and non-Windows users")

#标准化(有警告）建议用transform
def normed(group):
    group['normed']=group['value']/group['value'].sum()
    return group
#注意，如果要直接先存储求和后数据后相除，得用map才能对应上。transform直接返回原结构dataframe了
l_c_s_normed=long_count_subset.groupby('tz').apply(normed)
print('l_c_s_normed:\n',l_c_s_normed,sep="")
sns.barplot(x='normed',y='tz',hue='os',data=l_c_s_normed,ax=axes[1])
axes[1].set_title("Normalized Number of Users")





#分成windows、GoogleMaps/RochesterNY、iPad、Macintosh、iPhone
cframe2=frame[frame['a'].notna()].copy()
cframe2['a'].fillna("MISSING",inplace=True)
# 1. 定义你的条件列表
conditions = [
    cframe2["a"].str.contains("Windows", case=False), # case=False 表示不区分大小写
    cframe2["a"].str.contains("iPhone", case=False),
    cframe2["a"].str.contains("iPad", case=False),
    cframe2["a"].str.contains("GoogleMaps/RochesterNY", case=False),
    cframe2["a"].str.contains("Macintosh", case=False)
]
# 2. 定义与条件对应的结果列表
choices = [
    "Windows",
    "iPhone",
    "iPad",
    "GoogleMaps",
    "macOS"
]
# 3. 使用 np.select() 进行判断
#    - 如果条件1满足，赋值"Windows"
#    - 如果条件1不满足但条件2满足，赋值"iPhone"
#    - ...以此类推
#    - 如果所有条件都不满足，则赋值"Other"
cframe2['os'] = np.select(conditions, choices, default='Other')
print('cframe2[\'os\'].value_counts():\n',cframe2['os'].value_counts(),sep="")
print('cframe2:\n',cframe2,sep="")
#注意不要[cframe2['tz']==""]，这样整行都会改
cframe2.loc[cframe2['tz']=="",'tz']="UNKNOWN_ZONE"
#选出tz和os两列
cf2_subset=cframe2.loc[:,['tz','os']]
#分组并计数
print('cf2_subset:\n',cf2_subset,sep="")
gourped_tz_os=cf2_subset.groupby(['tz','os']).value_counts()
print('gourped_tz_os:\n',gourped_tz_os.head(40),sep="")
#找出设备最多的5大地区
gourped_tz_os_unstack=gourped_tz_os.unstack().fillna(0)
print("gourped_tz_os_unstack:\n",gourped_tz_os_unstack.head(20),sep="")
indexer2=gourped_tz_os_unstack.sum(axis=1).argsort()
#.copy()避免视窗和副本的警告
top_5_zone=gourped_tz_os_unstack.iloc[indexer2[-5:],:].copy()
#top_5_zone['total']=top_5_zone.sum(axis=1)
#print('top_5_zone:\n',top_5_zone,sep="")
#sns画图
fig2,ax2=plt.subplots(2,1,figsize=(16,9))
top_5_zone=top_5_zone.reset_index()
top_5_zone_melt=pd.melt(top_5_zone,id_vars='tz')
print('top_5_zone_melt:\n',top_5_zone_melt,sep="")
#绝对数量
sns.barplot(x='value',y='tz',hue='os',data=top_5_zone_melt,ax=ax2[0])
ax2[0].set_title("Number of various users")
#标准化数量占比
top_5_zone_melt['normed']=top_5_zone_melt['value']/top_5_zone_melt.groupby('tz')['value'].transform('sum')
print('top_5_zone_normed:\n',top_5_zone_melt)
sns.barplot(x='normed',y='tz',hue='os',data=top_5_zone_melt,ax=ax2[1])
ax2[1].set_title("Normalized Number of  Various Users")
plt.tight_layout()
plt.show()



