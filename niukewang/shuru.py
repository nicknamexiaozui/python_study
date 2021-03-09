#-- coding: utf-8 --
#@Time : 2021/3/9 8:54
#@Author : XXXX
#@Email : XXXX@qq.com
#@File : shuru.py
#@Software: PyCharm
'''
输入描述:
输入包括两个正整数a,b(1 <= a, b <= 10^9),输入数据包括多组。

输出描述:
输出a+b的结果

输入例子1:
1 5
10 20

输出例子1:
6
30
'''
import sys
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))
