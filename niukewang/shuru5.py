#-- coding: utf-8 --
#@Time : 2021/3/9 9:34
#@Author : XXXX
#@Email : XXXX@qq.com
#@File : shuru5.py
#@Software: PyCharm
'''
输入描述:
输入的第一行包括一个正整数t(1 <= t <= 100), 表示数据组数。
接下来t行, 每行一组数据。
每行的第一个整数为整数的个数n(1 <= n <= 100)。
接下来n个正整数, 即需要求和的每个正整数。

输出描述:
每组数据输出求和的结果

输入例子1:
2
4 1 2 3 4
5 1 2 3 4 5

输出例子1:
10
15
'''
n = int(input())
for i in range(n):
    a = list(map(int,input().split()))
    print(sum(a)-a[0])