#-- coding: utf-8 --
#@Time : 2021/3/9 9:05
#@Author : XXXX
#@Email : XXXX@qq.com
#@File : shuru3.py
#@Software: PyCharm
'''
输入包括两个正整数a,b(1 <= a, b <= 10^9),输入数据有多组, 如果输入为0 0则结束输入

输出描述:
输出a+b的结果

输入例子1:
1 5
10 20
0 0

输出例子1:
6
30
'''
import sys
for line in sys.stdin:
    a = line.split()
    if a[0] !='0':
        print(int(a[0]) + int(a[1]))
    else:
        break