import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

path='babynames/yob1880.txt'
names1880=pd.read_csv(path,names=["name", "sex", "births"])
print('names1880:\n',names1880,sep="")
#汇总所有数据
pieces=[]
for year in range(1880,2011):
    path=f'babynames/yob{year}.txt'
    frame=pd.read_csv(path,names=["name", "sex", "births"])
    frame['year']=year
    pieces.append(frame)
#可以将整个列表合并
names=pd.concat(pieces,ignore_index=True)
print('names:\n',names,sep="")
#透视表，作出每年出生人口图
names_pivot_year_sex=pd.pivot_table(names,index='year',columns='sex',aggfunc={'births':'sum'})
print('names_pivot_year_sex(每年出生男女）:\n',names_pivot_year_sex,sep="")
fig1,ax1=plt.subplots()
names_pivot_year_sex.plot(title="Total births by sex and year",ax=ax1)
#plt.show()
def add_prop(group):
    group['prop']=group['births']/group['births'].sum()
    return group

#不保留year、sex索引
names=names.groupby(['year','sex'],group_keys=False)[names.columns].apply(add_prop)
print("names加上比例：\n",names,sep="")
#每个性别/年份组合的前 1000 个名字
#在每个分组内部，对 births 列进行降序排序，然后取每个组的前 1000 名。
#top1000_ey_by_s=names.groupby(['year','sex']).sort_values('births',ascending=False)[:1000]#这个方法不行，DataFrameGroupBy无法使用sort_values。因为一旦sort_values，分组也就失去意义了
#因此，要实现 “分组内排序”，你需要使用 apply 函数，将排序操作应用到每个分组上后再排序
def get_top1000(group):
    group=group.sort_values('births',ascending=False)[:1000]
    return group
#[names.columns]避免futurewarning，group_keys=False丢弃分组索引
top1000_ey_by_s=names.groupby(['year','sex'],group_keys=False)[names.columns].apply(get_top1000)
print('top1000_ey_by_s:\n',top1000_ey_by_s,sep="")
boys = top1000_ey_by_s[top1000_ey_by_s["sex"] == "M"]
girls = top1000_ey_by_s[top1000_ey_by_s["sex"] == "F"]
births_by_yearAndname=top1000_ey_by_s.pivot_table('births',index='year',columns='name',aggfunc='sum')
print('births_by_yearAndname:\n',births_by_yearAndname,sep="")
print("births_by_yearAndname.info()",births_by_yearAndname.info(),sep="")
subset = births_by_yearAndname[["John", "Harry", "Mary", "Marilyn"]]
#subplots=True参数，让每一列数据都作子图
subset.plot(subplots=True, figsize=(12, 10),title="Number of births per year")

#分析前1000个名字的多样性
top1000_prop=top1000_ey_by_s.pivot_table('prop',index='year',columns='sex',aggfunc='sum')
top1000_prop.plot(title="Sum of table1000.prop by year and sex",yticks=np.linspace(0, 1.2, 13))
#前50%人数的名字的多样程度
def get_quantile_count(group,q=0.5):
    group=group.sort_values('prop',ascending=False)
    return group['prop'].cumsum().searchsorted(q)+1
diversity=top1000_ey_by_s.groupby(['year','sex'])[top1000_ey_by_s.columns].apply(get_quantile_count)
diversity = diversity.unstack()
print('diversity:\n',diversity,sep="")
diversity.plot(title="Number of popular names in top 50%")
plt.show()