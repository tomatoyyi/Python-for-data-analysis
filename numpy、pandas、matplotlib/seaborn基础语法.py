import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# s = pd.Series(np.random.standard_normal(10).cumsum(), index=np.arange(0,
#  100, 10))
# s.plot(kind='line')
# plt.show()

# df = pd.DataFrame(np.random.standard_normal((10, 4)).cumsum(0),columns=["A", "B", "C", "D"],index=np.arange(0, 100, 10))
# df.plot(subplots=True,sharex=True)
# plt.show()

# #条形图
# df = pd.DataFrame(np.random.uniform(size=(6, 4)),index=["one", "two", "three", "four", "five", "six"],columns=pd.Index(["A", "B", "C", "D"], name="Genus"))
# df.plot.bar()
# plt.show()

# #用画布
# fig, axes = plt.subplots(2, 1)
# data = pd.Series(np.random.uniform(size=16), index=list("abcdefghijklmnop"))
# data.plot.bar(ax=axes[0], color="black", alpha=0.7)
# data.plot.barh(ax=axes[1], color="black", alpha=0.7)
# plt.show()