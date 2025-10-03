import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option("display.width", 1000)


#这个数据集把所有数据放在一行,与前面不一样，不可records = [json.loads(line) for line in f]
path='usda_food/database.json'
#dataset是一个列表，一个数据对应一个字典
dataset=json.load(open(path))
#print(json.dumps(dataset[0], ensure_ascii=False, indent=4))
print(f'数据条数：{len(dataset)}条')
print("每条数据的键：",dataset[0].keys())
info_keys = ["description", "group", "id", "manufacturer"]
#用字典创造df数据，可用columns控制需要的键值对
info=pd.DataFrame(dataset,columns=info_keys)
print('info:\n',info,sep="")
#用info看看有无缺失数据
print("info.info():")
info.info()
#取到营养的数据
nutrients=[]
for rec in dataset:
    fnutr=pd.DataFrame(rec['nutrients'])
    fnutr['id'] = rec['id']
    nutrients.append(fnutr)
nutrients=pd.concat(nutrients,ignore_index=True)
print('nutrients:\n',nutrients,sep="")
#查看是否有重复项
print('nutrients重复数目：',nutrients.duplicated().sum(),sep="")
#处理重复
nutrients = nutrients.drop_duplicates()
#改列名防止歧义
info_col_mapping = {"description" : "food","group"       : "fgroup"}
info.rename(columns=info_col_mapping, copy=False, inplace=True)
nutr_col_mapping = {"description" : "nutrient","group" : "nutgroup"}
nutrients.rename(columns=nutr_col_mapping, copy=False, inplace=True)
ndata = pd.merge(nutrients, info, on="id")
ndata.info()
print("合并后数据：\n",ndata,sep="")
#注意，quantile返回的是一个Series，且有二级索引，因此result["Zinc, Zn"]才能选出所有一级索引为"Zinc, Zn"
#找出某个营养成分在各类食物组中的中值
nutrient_mid_result = ndata.groupby(["nutrient", "fgroup"])["value"].quantile(0.5)
print('nutrient_mid_result:\n',nutrient_mid_result,sep="")
nutrient_mid_result["Zinc, Zn"].sort_values().plot(kind="barh")
def re_max(group):
    return group.loc[group.value.idxmax()]
gb_nutg_nutr=ndata.groupby(['nutgroup','nutrient']).apply(re_max,include_groups=True)[["value", "food"]]
#查看各个食物含氨基酸类最多的食物
print('gb_nutg_nutr.loc["Amino Acids"]["food"]:\n',gb_nutg_nutr.loc["Amino Acids"]["food"],sep="")
plt.show()