
# a=[1,2,3]
# b=a
# print('a=',a)
# print('a的类型=',type(a))
# print('a的地址=',id(a))
# print('b的地址=',id(b))
# print(f'a is {type(a)},b is {type(b)}')

#strftime 和strptime
# from datetime import datetime
# now=datetime.now()
# print(now.strftime("%Y-%m-%d %H:%M"))
# date1=datetime.strptime('20250920','%Y%m%d')
# print(date1.date())

# #range
# from datetime import datetime
# a=list(range(0,10,2))
# print(a)
# print(2 in a)
# b=list(range(10,20,2))
# print(b)
# now1=datetime.now()
# a.extend(b)
# now2=datetime.now()
# print(now2-now1)
# print(a)
# now1=datetime.now()
# for chunk in b:
#     a.append(chunk)
# now2=datetime.now()
# print(now2-now1)
# print(a)
# now1=datetime.now()
# a=a+b
# now2=datetime.now()
# print(now2-now1)
# print(a)

#用列表创建字典
list1=[('a',1),('b',2),('c',3)]
dict1=dict(list1)
print(dict1)
#推导生成字典
dict2={key:value for key,value in list1}
print(dict2)
