import numpy as ny
#创建一维数组
# a=ny.array([1,2,3,4,5])
# #创建二维数组
# b=ny.array([[1,2,3,4,5],[1,2,3,4,5]])#类似于MATLAB中的矩阵
# a.sort()   #sorted函数能够排序同时不改变原数组
# b.sort()   #reverse等于 true或者false参数实现排序大小
# c=a.max() #max min
# d=b.max()
# #切片
# #数组[起始下标：最终下表+1]
# e=a[1:3] #取值为第二个第三个  1，2
# f=a[:3]
# g=a[1:]
# print(a[1]) #输出第二个元素
# print(b[1][1])#输出二行二列元素
# print(a)
# print(b)
# print(e)
# print(f)
# print(g)

import pandas as pda

# a=pda.Series([8,9,2,1])
# b=pda.Series([8,9,2,1],index=["one","two","three","four"])
# c=pda.DataFrame([[5,6,2,3],[8,4,6,3],[6,4,32,1]])
# d=pda.DataFrame([[5,6,2,3],[8,4,6,3],[6,4,31,2]],columns=["one","two","three","four"])
# e=pda.DataFrame({
#     "one":4,
#     "two":[6,2,3],
#     "three":list(str(983))
# })
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(d.head()) #默认取头部前五行，括号里可以加参数
# print(d.tail())#尾部数据，默认后五行，括号里可以加参数
# print(d.describe()) #显示结构数据 其中百分数表示分位数，也就是几等分的点
# print(d.T) #转置

# data=pda.read_csv("/Volumes/nothing but ordinal/spark/data_test.csv")
# print(data.describe())
# print(data.sort_values(by="4446")) #按照索引进行排序
# data1=pda.read_excel("")
# # 导入mysql中的数据
# import pymysql
# Connection=pymysql.connect(host="127.0.0.1",user="root",passwd="root",db="hexun")
# sql="select * from sss"
# data2=pda.read_sql(sql,Connection)
#
# # pandas可以读取html中的表格但是得安装 html5lib beautifulsoup4
# data3=pda.read_html()
# data4=pda.read_table()#读取文本信息

import matplotlib.pylab as plt
import numpy as npy
#折线图 matplotlib.pylab
x=[1,2,3,4,8]
y=[5,7,2,3,1]
plt.subplot(211)
plt.plot(x,y,'oy') #散点图，颜色为黄
plt.subplot(212)
plt.plot(x,y,'c')
# c-cyan-青色
# r-red--红色
# m-magente-一瓶红
# g-green-绿色
# b    蓝色
# y    黄色
# b    黑色
# 线条样式
'''-直线
   --虚线
   -.-.形式
   ：细小虚线
   
s-方形
h-六角形
*-星型
+ 加号
x x型
d 菱形
p 五角形
  


'''

plt.title('show')
plt.xlabel('ages')
plt.ylabel('temp')
plt.xlim(0,1)
plt.ylim(0,18)
plt.show()


