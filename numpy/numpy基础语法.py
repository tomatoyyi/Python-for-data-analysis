import numpy as np

arr1=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print('arr1:\n',arr1)
print('arr1\'s dim=',arr1.ndim)
print('arr1\'s shape=',arr1.shape)
print('arr1\'s size=',arr1.size)
print('arr1\'s dtype=',arr1.dtype)
arr2=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=np.float64)
print('arr2:\n',arr2)
arr3=arr2.astype(np.int64)
print('arr3:\n',arr3)
print('arr2*arr3:\n',arr2*arr3)
arr4=np.random.randint(0,100,9).reshape(3,3)
print('arr4:\n',arr4)
print('arr2*arr3>arr4:\n',(arr2*arr3)>arr4)
#变量赋值很像“引用”，除非用方法copy
arr5=arr4
arr5[2:5]=[100,101,102]
print('arr5:\n',arr5)
print('arr4:\n',arr4)
arr6=arr4.copy()
arr6=0
print('arr6:\n',arr6)
print('arr4:\n',arr4)
arr_3d_1=np.random.randint(0,100,12).reshape(2,2,3)
print('arr_3d_1:\n',arr_3d_1)
print('arr_3d_1[1][0]=',arr_3d_1[1][0])
print('arr_3d_1[1,0]=',arr_3d_1[1,0])
#切片
print('arr_3d_1[:,:1,:2]:\n',arr_3d_1[:,:1,:2])
#Bool索引
names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"])
data = np.array([[4, 7], [0, 2], [-5, 6], [0, 0], [1, 2], [-12, -4], [3, 4]])
#一个人名对应一行，让Bob和Joes对应的行都显示
index=(names == "Bob")|(names == "Joe")
print('index=',index)
print('data[index,:1]:\n',data[index,:1])
#Bool索引
print('data:\n',data)
print('data<0=',data<0)
print('data[data<0]=',data[data<0])
#花式索引
arr7 = np.zeros((8, 4))

for i in range(8):
     arr7[i] = i

print('arr7:\n',arr7)
print('arr7[[4,3,0,6]]:\n',arr7[[4,3,0,6]])
#多个书的索引
arr8=np.arange(32).reshape(8,4)
print('arr8:\n',arr8)
print('arr8[[1, 5, 7, 2], [0, 3, 1, 2]]=',arr8[[1, 5, 7, 2], [0, 3, 1, 2]])

