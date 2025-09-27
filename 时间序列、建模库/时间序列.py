import numpy as np
import pandas as pd
from datetime import datetime
import pytz
import matplotlib.pyplot as plt

# now=datetime.now()
# print('now:',now)
# print(type(now))
# print(now.strftime("%Y-%m-%d %H:%M:%S:%f"))
# print(now.strftime("%F"))

# dates = [datetime(2011, 1, 2), datetime(2011, 1, 5),datetime(2011, 1, 7), datetime(2011, 1, 8),datetime(2011, 1, 10), datetime(2011, 1, 12)]
# df1=pd.DataFrame(np.random.standard_normal(6),index=pd.to_datetime(dates),columns=["a"])
# print('df1.index:',df1.index)
# print('df1:\n',df1,sep="")

# #生成日期范围
# index1=pd.date_range('2025-05-08','2025-06-08',freq='B')
# print('index1:\n',index1,sep="")
# index2=pd.date_range(end="2012-06-01", periods=20)
# print('index2:\n',index2,sep="")

# stamp = pd.Timestamp("2011-03-12 04:00")
# print(stamp)
# p = pd.Period("2011Q1", freq="Q-MAR")  # 代表 2010-04-01 ~ 2010-06-30的一个范围

# #重采样
# data=pd.DataFrame(np.random.standard_normal((100,5)),index=pd.date_range(pd.Timestamp.now(),periods=100),columns=['A','B','C','D','E'])
# print('data:\n',data,sep="")
# print("data.resample('ME').mean():\n",data.resample('ME').mean(),sep="")
# data_period_index = data.to_period('M')
# print("data_period_index:\n",data_period_index,sep="")
# #转换后的数据仍然是多行，只是同一月份的行共享同一个 “月时期标签”—— 这一步并没有做 “聚合计算”，只是做了 “时间标签的归类”。
# #resample('M') 的核心作用是 “按指定的时间频率（这里是‘月’），将同一频率组内的多行数据聚合为一行”，而 .mean() 是聚合时用的 “计算规则”（求平均值）。
# #resample的核心作用：解决 “标签重复” 问题、明确 “聚合维度”：告诉 Pandas“按‘月’这个维度进行聚合”，而不是按全局、按日或其他维度；
# print("data_period_index.mean():\n",data_period_index.mean(),sep="")
# print("data_period_index.groupby(level=0).mean():\n",data_period_index.groupby(level=0).mean(),sep="")

# #下采样
# dates = pd.date_range("2000-01-01", periods=12, freq="min")
# ts = pd.Series(np.arange(len(dates)), index=dates)
# print('ts:\n',ts,sep="")
# #整合成5分钟
# print('ts.resample("5min").mean():\n',ts.resample("5min").mean(),sep="")

# #按周期重采样
# frame = pd.DataFrame(np.random.standard_normal((24, 4)),index=pd.period_range("1-2000", "12-2001",freq="M"),columns=["Colorado", "Texas", "New York", "Ohio"])
# print(frame.head())
# annual_frame = frame.resample("A-DEC").mean()
# print(annual_frame)
# print("annual_frame.resample(\"Q-DEC\").ffill():\n",annual_frame.resample("Q-DEC").ffill(),sep="")
# #原本的时间段被作为2000开始和结束的两端。当开始的2000降采样落到2000Q4，就不会显示前面三个季度
# print('annual_frame.resample("Q-DEC", convention="end").asfreq():\n',annual_frame.resample("Q-DEC", convention="end").asfreq().index,sep="")

# pt=pd.Period("2011",freq="Q-MAR")
# print(pt)
# p = pd.Period("2011", freq="A-DEC")
# print(p)
# #另外由 定义的时间跨度Q-MAR仅与A-MAR、A-JUN、A-SEP和A-DEC一致，因为只有这样时间点才能对齐

#移动函数
sa=list()
start_time = pd.Timestamp.now()

for i in range(4):
    new_series = pd.Series(
        np.random.standard_normal(1000).cumsum(),
        index=pd.date_range(start_time, periods=1000)
    )
    # 使用 .append() 将新创建的 Series 添加到列表 sa 的末尾
    sa.append(new_series)
#print(sa)
df=pd.DataFrame(sa).T
df.columns=list("ABCD")
df=df.resample("D").asfreq()
print(df)
fig,ax=plt.subplots(2,1)
for column in df.columns:
    ax[0].plot(df.index,df[column],label=column)
ax[0].legend()
quarterly_dates = pd.date_range(start=df.index[0], end=df.index[-1], freq='6MS')
ax[0].set_xticks(ticks=quarterly_dates)
ax[0].set_xticklabels(quarterly_dates.strftime("%Y-%m"))
df250=df.rolling(window=250).mean()
for column in df250.columns:
    ax[1].plot(df.index, df250[column], label=column)
ax[1].legend()
quarterly_dates = pd.date_range(start=df250.index[0], end=df250.index[-1], freq='6MS')
ax[1].set_xticks(ticks=quarterly_dates)
ax[1].set_xticklabels(quarterly_dates.strftime("%Y-%m"))
df250=df250.dropna()
print(df250)
plt.show()
