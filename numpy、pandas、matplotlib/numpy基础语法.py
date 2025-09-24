import numpy as np

# arr1=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# print('arr1:\n',arr1)
# print('arr1\'s dim=',arr1.ndim)
# print('arr1\'s shape=',arr1.shape)
# print('arr1\'s size=',arr1.size)
# print('arr1\'s dtype=',arr1.dtype)
# arr2=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=np.float64)
# print('arr2:\n',arr2)
# arr3=arr2.astype(np.int64)
# print('arr3:\n',arr3)
# print('arr2*arr3:\n',arr2*arr3)
# arr4=np.random.randint(0,100,9).reshape(3,3)
# print('arr4:\n',arr4)
# print('arr2*arr3>arr4:\n',(arr2*arr3)>arr4)
# #变量赋值很像“引用”，除非用方法copy
# arr5=arr4
# arr5[2:5]=[100,101,102]
# print('arr5:\n',arr5)
# print('arr4:\n',arr4)
# arr6=arr4.copy()
# arr6=0
# print('arr6:\n',arr6)
# print('arr4:\n',arr4)
# arr_3d_1=np.random.randint(0,100,12).reshape(2,2,3)
# print('arr_3d_1:\n',arr_3d_1)
# print('arr_3d_1[1][0]=',arr_3d_1[1][0])
# print('arr_3d_1[1,0]=',arr_3d_1[1,0])
# #切片
# print('arr_3d_1[:,:1,:2]:\n',arr_3d_1[:,:1,:2])
# #Bool索引
# names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"])
# data = np.array([[4, 7], [0, 2], [-5, 6], [0, 0], [1, 2], [-12, -4], [3, 4]])
# #一个人名对应一行，让Bob和Joes对应的行都显示
# index=(names == "Bob")|(names == "Joe")
# print('index=',index)
# print('data[index,:1]:\n',data[index,:1])
# #Bool索引
# print('data:\n',data)
# print('data<0=',data<0)
# print('data[data<0]=',data[data<0])
# #花式索引
# arr7 = np.zeros((8, 4))
# for i in range(8):
#      arr7[i] = i
# print('arr7:\n',arr7)
# print('arr7[[4,3,0,6]]:\n',arr7[[4,3,0,6]])
# #多个书的索引
# arr8=np.arange(32).reshape(8,4)
# print('arr8:\n',arr8)
# print('arr8[[1, 5, 7, 2], [0, 3, 1, 2]]=',arr8[[1, 5, 7, 2], [0, 3, 1, 2]])

# #伪随机数生成
# #标准正态分布
# samples1=np.random.standard_normal(size=(5,5))
# print('samples1:\n',samples1)
# #随机数生成器
# rng=np.random.default_rng(seed=250921)
# samples2=rng.standard_normal(size=(5,5))
# print('samples2:\n',samples2)
# samples3=np.random.permutation(samples2)
# print('samples3:\n',samples3)
# #通用函数
# x=rng.standard_normal(5)
# print('x=',x)
# y=rng.standard_normal(5)
# print('y=',y)
# print('np.maximum(x,y)=',np.maximum(x,y))
# #假设我们有两个数组 a 和 b，想计算它们的和，并且把结果存到已经存在的数组 c 中，而不是生成一个新数组。
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# # 预先创建一个用于存储结果的数组 c
# c = np.zeros_like(a)
# # 使用 out 参数，将 a + b 的结果直接存入 c
# np.add(a, b, out=c)
# print('c=',c)

# #条件逻辑表达为数组运算
# arr9=np.random.standard_normal((5,5))*100
# print('arr9:\n',arr9)
# #意图把小于零的数都改为零
# con=arr9<0
# print('con:\n',con)
# arr9=np.where(con,0,arr9)
# print('arr9:\n',arr9)

# #数学和统计方法
# arr10=np.arange(12).reshape(3,4)
# print('arr10:\n',arr10)
# print('arr10.sum=',arr10.sum())
# print('arr10.sum(axis=1)=',arr10.sum(axis=1))#往列增加的方向加总
# print('arr10.sum(axis=0)=',arr10.sum(axis=0))#往行增加的方向加总
# arr11=np.random.standard_normal((3,4))
# print('arr11:\n',arr11)
# #计算大于零的个数
# print('(arr11>0).sum()=',(arr11>0).sum())

# #随机游走
# nwalks=500
# nsteps=1000
# bt=30
# arr12=np.random.randint(0,2,size=(nwalks,nsteps))
# arr12=np.where(arr12>0,1,-1)
# #累计起来
# walks=arr12.cumsum(axis=1)
# print(walks)
# #找出离开原点有超过bt步的行
# con_bt=(np.abs(walks)>bt).any(axis=1)
# print('超过30步的行有：',con_bt.sum())
# #找出这些能超过bt步的行最短时间,argmax返回第一个最大值的索引就是
# bt_s_time=(np.abs(walks[con_bt])>bt).argmax(axis=1)
# print(bt_s_time)
# print('平均走了：',bt_s_time.mean())



# #高级功能
# rng = np.random.default_rng(seed=12345)
# #C风格
# arr1=np.arange(12).reshape(3,4,order='C')
# #FORTRAN风格
# arr2=np.arange(12).reshape(3,4,order='F')
# print('arr1:\n',arr1)
# print('arr2:\n',arr2)
# #展平
# print('arr1.ravel()=',arr1.ravel())
# #take和put的使用
# index=[1,3]
# line1=np.arange(10)
# print('line1.take(index)=',line1.take(index))
# line2=line1
# #put改变原数组
# line2.put(index,[100,200])
# print('line2=',line2)
# arr3=rng.integers(0,10,(4,5))
# print('arr3:\n',arr3)
# print('arr3.take(index,axis=1):\n',arr3.take(index,axis=1))

# #广播
# mat=np.random.randint(0,10,(4,5))
# print('mat:\n',mat)
# row_mean=mat.mean(1).reshape(4,1)
# print('row_mean:\n',row_mean)
# print('mat-row_mean:\n',mat-row_mean)

#ufunc
arr1=np.arange(9).reshape(3,-1) #-1自动运算
print('arr1:\n',arr1)
print('np.add.reduce(arr1,axis=1)=',np.add.reduce(arr1,axis=1))
print('np.multiply.reduce(arr1,axis=1)=',np.multiply.reduce(arr1,axis=1))
#自定义ufunc
def add_ele(x,y):
    return x+y
#2是参数数量，1是返回值数量
add_them=np.frompyfunc(add_ele,2,1)
print('add_them(np.arange(5),np.arange(5))=',add_them(np.arange(5),np.arange(5)))