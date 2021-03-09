#-- coding: utf-8 --
#@Time : 2021/3/9 10:22
#@Author : XXXX
#@Email : XXXX@qq.com
#@File : shuru10.py
#@Software: PyCharm
'''
输入描述:
多个测试用例，每个测试用例一行。每行通过,隔开，有n个字符，n＜100

输出描述:
对于每组用例输出一行排序后的字符串，用','隔开，无结尾空格

输入例子1:
a,c,bb
f,dddd
nowcoder

输出例子1:
a,bb,c
dddd,f
nowcoder
'''
while True:
    try:
        a=input().split(',')
        # a=a.split(',')
        a.sort()
        for i in range(len(a)-1):
            print(a[i],end=',')
        print(a[-1])
    except:break