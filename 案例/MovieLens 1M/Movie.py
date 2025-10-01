import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)

unames = ["user_id", "gender", "age", "occupation", "zip"]
users = pd.read_table("movielens/users.dat", sep="::",
                      header=None, names=unames, engine="python")
print('users.head():\n', users.head(),sep="")
rnames = ["user_id", "movie_id", "rating", "timestamp"]
ratings = pd.read_table("movielens/ratings.dat", sep="::",
                        header=None, names=rnames, engine="python")
print('ratings.head():\n', ratings.head(),sep="")
mnames = ["movie_id", "title", "genres"]
movies = pd.read_table("movielens/movies.dat", sep="::",
                       header=None, names=mnames, engine="python")
print('movies.head():\n', movies.head(),sep="")
#进行多对一的连接
data=pd.merge(pd.merge(ratings, users, on="user_id"),movies, on="movie_id")
print('data.head(20):\n', data.head(20),sep="")

mean_ratings_by_gender=data.pivot_table(index='title',columns='gender',values='rating',aggfunc={'rating':'mean'})
#print(data.groupby(["title","gender"])['rating'].mean().unstack())#另一透视方法
print('mean_ratings_by_gender:\n',mean_ratings_by_gender,sep="")
#获取至少有250个评分的电影进行分析
groupby_title=data.groupby('title').size()
#获取指数，再用loc取到数据
#设置有效评分数量
amount=250
active_titles=groupby_title[groupby_title>=amount].index
print("active_titles:\n",active_titles,sep="")
active_titles_mr_gb_gender=mean_ratings_by_gender.loc[active_titles]
print("active_titles_mr_gb_gender:\n",active_titles_mr_gb_gender,sep="")
top_female_ratings = active_titles_mr_gb_gender.sort_values("F", ascending=False)
print("top_female_ratings:\n",top_female_ratings,sep="")
#衡量评级分歧(绝对分值）
#更受到女性青睐的
active_titles_mr_gb_gender['abs_diff']=active_titles_mr_gb_gender['F']-active_titles_mr_gb_gender['M']
sorted_by_diff=active_titles_mr_gb_gender.sort_values("abs_diff", ascending=False)
print("sorted_by_diff(女性喜欢男不喜欢）:\n",sorted_by_diff,sep="")
print("sorted_by_diff(男性喜欢女不喜欢）:\n",sorted_by_diff[::-1],sep="")
#衡量评级分歧(相对位置）
rank_by_F=active_titles_mr_gb_gender.sort_values("F",ascending=False).reset_index()
rank_by_F['rank']=np.arange(1, len(rank_by_F)+1)
rank_by_M=active_titles_mr_gb_gender.sort_values("M",ascending=False).reset_index()
rank_by_M['rank']=np.arange(1, len(rank_by_M)+1)
#print("rank_by_M:\n",rank_by_M,sep="")
active_titles_mr_gb_gender=pd.merge(active_titles_mr_gb_gender, rank_by_M.loc[:,['title','rank']], left_index=True,right_on="title", how="inner")
active_titles_mr_gb_gender=pd.merge(active_titles_mr_gb_gender, rank_by_F.loc[:,['title','rank']], on="title", how="inner",suffixes=("_M","_F"))
active_titles_mr_gb_gender.set_index('title', inplace=True,drop=True)
active_titles_mr_gb_gender['rank_diff']=active_titles_mr_gb_gender['rank_M']-active_titles_mr_gb_gender['rank_F']
print("排名差距最大的10部电影（女高男低）:\n",active_titles_mr_gb_gender.sort_values('rank_diff',ascending=False)[:10],sep="")
print("排名差距最大的10部电影（男高女低）:\n",active_titles_mr_gb_gender.sort_values('rank_diff',ascending=False)[-10::],sep="")


#分析各年龄段喜爱的类别
#拆分电影类别
# 可行的一种思路,比较耗时
#title_genres=pd.Series(movies['genres'])
#title_genres=title_genres.rename(index=movies['title'])
#pop方法把原数据去掉
movies["genre"] = movies.pop("genres").str.split("|")
#.explode("genre")会生成一个新的 DataFrame，每个列表中的每个“内部”元素对应一行,且其他列一同复制。
movies_exploded=movies.explode('genre')
print('movies_exploded.head(10):\n', movies_exploded.head(10))
#合并三大表
ratings_with_genre=pd.merge(pd.merge(movies_exploded,ratings, on="movie_id"), users, on="user_id")
print('ratings_with_genre.head(10):\n',ratings_with_genre.head(10))
ratings_with_genre['age'].astype('category')
bins=[0,18,35,55,100]
labels=['teen','youth','middle','aged']
ratings_with_genre['age']=pd.cut(ratings_with_genre['age'], bins=bins, labels=labels,right=False)
ratings_with_genre.groupby(['age','genre'],observed=True)
ratings_with_genre_pt=pd.pivot_table(data=ratings_with_genre, values='rating', index=['genre'], columns=['age'],aggfunc={'rating':'mean'},observed=True)
pd.set_option('display.colheader_justify', 'left')

print('ratings_with_genre_pt.head(10):\n',ratings_with_genre_pt.head(10),sep="")
df=list()
for i,group in enumerate(labels):
    print(f"{group}最喜欢的十大类别：\n",ratings_with_genre_pt.sort_values(group,ascending=False).loc[:,group][0:10],sep="")
    df.append(ratings_with_genre_pt.sort_values(group, ascending=False).loc[:, group][0:10].reset_index())
    df[i].rename(columns={'group': 'rating'}, inplace=True)
    new_columns = [(group, 'genre'), (group, 'rating')]
    # 使用 from_tuples 创建 MultiIndex
    df[i].columns = pd.MultiIndex.from_tuples(new_columns)
dfcon=df[0]
for i in range (0,len(df)-1):
    dfcon=pd.concat([dfcon,df[i+1]],axis=1)

print("各年龄段最爱的十大电影：\n",dfcon,sep="")