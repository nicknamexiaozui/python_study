#-- coding: utf-8 --
#@Time : 2021/3/9 10:08
#@Author : XXXX
#@Email : XXXX@qq.com
#@File : shuru9.py
#@Software: PyCharm
'''
输入描述:
多个测试用例，每个测试用例一行。每行通过空格隔开，有n个字符，n＜100

输出描述:
对于每组测试用例，输出一行排序过的字符串，每个字符串通过空格隔开

输入例子1:
a c bb
f dddd
nowcoder

输出例子1:
a bb c
dddd f
nowcoder
'''
while True:
    try:
        a=input().split()
        a.sort()
        for i in a:
            print(i,end=' ')
        print()
    except:break