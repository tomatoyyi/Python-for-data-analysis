import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# import json
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_colwidth', None)
# pd.set_option("display.width", 1000)
 
fec = pd.read_csv("D:/PythonProject/data/fec/P00000001-ALL.csv", low_memory=False)
fec.info()
#获取所有唯一政治候选人的列表
unique_cands = fec["cand_nm"].unique()
print("候选人列表：",unique_cands)
#添加党派信息
parties = {"Bachmann, Michelle": "Republican",
           "Cain, Herman": "Republican",
           "Gingrich, Newt": "Republican",
           "Huntsman, Jon": "Republican",
           "Johnson, Gary Earl": "Republican",
           "McCotter, Thaddeus G": "Republican",
           "Obama, Barack": "Democrat",
           "Paul, Ron": "Republican",
           "Pawlenty, Timothy": "Republican",
           "Perry, Rick": "Republican",
           "Roemer, Charles E. 'Buddy' III": "Republican",
           "Romney, Mitt": "Republican",
           "Santorum, Rick": "Republican"}
fec["party"] = fec["cand_nm"].map(parties)
#查看献金和退款
print('献金和退款:\n',(fec["contb_receipt_amt"] > 0).value_counts())
fec = fec[fec["contb_receipt_amt"] > 0]
#仅查看奥巴马和罗姆尼两位主要候选人
fec_mrbo = fec[fec["cand_nm"].isin(["Obama, Barack", "Romney, Mitt"])]
print("仅查看奥巴马和罗姆尼两位主要候选人：\n",fec_mrbo,sep="")
#查看职业都有哪些
print("捐款人职业和捐款次数：\n",fec["contbr_occupation"].value_counts()[:20])

#将一个职业映射到另一个职业来清理其中一些职业的技巧；请注意使用这个“技巧”，dict.get允许没有映射的职业“通过”
occ_mapping = {
   "INFORMATION REQUESTED PER BEST EFFORTS" : "NOT PROVIDED",
   "INFORMATION REQUESTED" : "NOT PROVIDED",
   "INFORMATION REQUESTED (BEST EFFORTS)" : "NOT PROVIDED",
   "C.E.O.": "CEO"
}

def get_occ(x):
    # 用get方法，如果找到返回值，如果没找到返回x，防止程序中断
    return occ_mapping.get(x, x)

fec["contbr_occupation"] = fec["contbr_occupation"].map(get_occ)
# 为雇主做同样的事情：
emp_mapping = {
   "INFORMATION REQUESTED PER BEST EFFORTS" : "NOT PROVIDED",
   "INFORMATION REQUESTED" : "NOT PROVIDED",
   "SELF" : "SELF-EMPLOYED",
   "SELF EMPLOYED" : "SELF-EMPLOYED",
}

def get_emp(x):

    return emp_mapping.get(x, x)

fec["contbr_employer"] = fec["contbr_employer"].map(get_emp)
#按政党和职业汇总数据，然后筛选出总体捐款至少 200 万美元的子集
by_occupation = fec.pivot_table("contb_receipt_amt", index="contbr_occupation",columns="party", aggfunc="sum")
print("by_occupation:\n",by_occupation,sep="")
#进行行加总。因为可能一个职业中有人投民主，有人投共和
over_2mm = by_occupation[by_occupation.sum(axis="columns") > 2000000]
print("over_2mm:\n",over_2mm,sep="")
over_2mm=over_2mm.reset_index()
print("reset_index:\n",over_2mm)
long_over_2mm=pd.melt(over_2mm,id_vars='contbr_occupation')
sns.barplot(x='value',y='contbr_occupation',hue='party',data=long_over_2mm)

#找出向这两位主要候选人捐款最多的几个职业
def get_top_amounts(group,categ,n=10):
    grouped = group.groupby(categ)["contb_receipt_amt"].sum()
    return grouped.nlargest(n)
#先按候选人分组，才能按一个一个候选人传入
grouped=fec_mrbo.groupby("cand_nm").apply(get_top_amounts,"contbr_occupation", n=7,include_groups=False)
print('捐款前位的职业:\n',grouped,sep="")
#捐款金额分级
bins = np.array([0, 1, 10, 100, 1000, 10000,100_000, 1_000_000, 10_000_000])
amount_cut=pd.cut(fec_mrbo["contb_receipt_amt"], bins)
#observed=False (默认行为): 即使某些类别在数据中没有出现，也会为所有预定义的类别创建分组。
#observed=True: 只对数据中实际出现过的类别进行分组。
amount_rank=fec_mrbo.groupby(["cand_nm", amount_cut],observed=False)
print("各个金额等级人数：\n",amount_rank.size().unstack(level=0),sep="")
#标准化进行对比
bucket_sums = amount_rank["contb_receipt_amt"].sum().unstack(level=0)
print("bucket_sums:\n",bucket_sums,sep="")
normed_sums = bucket_sums.div(bucket_sums.sum(axis="columns"),axis="index")
print("normed_sums:\n",normed_sums,sep="")
normed_sums.plot(kind="barh")
plt.show()
