import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# #图像和子图
# fig=plt.figure()
# ax1 = fig.add_subplot(2, 2, 1)
# ax1.plot([1, 2, 3], [4, 5, 1],color="red",linestyle="--",label="first line")
# ax1.plot([1,2,3],[7,5,3],color="blue",linestyle="--",label="second line",marker='o')
# #显示图例
# ax1.legend()
# ax2=fig.add_subplot(2, 2, 4)
# ax3 = fig.add_subplot(2, 2, 3)
# plt.show()

#刻度、标签和图例
fig,ax=plt.subplots()
ax.plot(np.random.standard_normal(1000).cumsum())
ax.set(title="my first plt",xlabel="steps",ylabel="cumulative sum")
ax.set_xticks([0, 250, 500, 750, 1000])
ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'],rotation=30,fontsize=8)
plt.show()