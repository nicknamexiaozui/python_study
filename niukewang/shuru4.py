#-- coding: utf-8 --
#@Time : 2021/3/9 9:09
#@Author : XXXX
#@Email : XXXX@qq.com
#@File : shuru4.py
#@Software: PyCharm
'''
输入数据包括多组。
每组数据一行,每行的第一个整数为整数的个数n(1 <= n <= 100), n为0的时候结束输入。
接下来n个正整数,即需要求和的每个正整数。

输出描述:
每组数据输出求和的结果

输入例子1:
4 1 2 3 4
5 1 2 3 4 5
0

输出例子1:
10
15
'''
import sys
for line in sys.stdin:
    a = line.split()
    sum=0
    if a[0] !='0':
        for i in range(int(a[0])):
            sum=sum+int(a[i+1])
        print(sum)
    else:break