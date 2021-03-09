#-- coding: utf-8 --
#@Time : 2021/3/9 10:00
#@Author : XXXX
#@Email : XXXX@qq.com
#@File : shuru7.py
#@Software: PyCharm
'''
输入描述:
输入数据有多组, 每行表示一组输入数据。

每行不定有n个整数，空格隔开。(1 <= n <= 100)。

输出描述:
每组数据输出求和的结果

输入例子1:
1 2 3
4 5
0 0 0 0 0

输出例子1:
6
9
0
'''
import sys
for line in sys.stdin:
    a = list(map(int,line.split()))
    print(sum(a))