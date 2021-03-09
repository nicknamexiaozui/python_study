#-- coding: utf-8 --
#@Time : 2021/3/9 10:02
#@Author : XXXX
#@Email : XXXX@qq.com
#@File : shuru8.py
#@Software: PyCharm
'''
输入描述:
输入有两行，第一行n

第二行是n个空格隔开的字符串

输出描述:
输出一行排序后的字符串，空格隔开，无结尾空格

输入例子1:
5
c d a bb e

输出例子1:
a bb c d e
'''
a=int(input())
b=input().split()
b.sort()
for i in range(a):
    print(b[i],end=' ')