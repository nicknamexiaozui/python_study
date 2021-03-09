#-- coding: utf-8 --
#@Time : 2021/3/9 8:58
#@Author : XXXX
#@Email : XXXX@qq.com
#@File : shuru2.py
#@Software: PyCharm
'''
输入第一行包括一个数据组数t(1 <= t <= 100)
接下来每行包括两个正整数a,b(1 <= a, b <= 10^9)

输出描述:
输出a+b的结果

输入例子1:
2
1 5
10 20

输出例子1:
6
30
'''
n = int(input())
for i in range(n):
    n = input().split()
    print(int(n[0])+int(n[1]))
