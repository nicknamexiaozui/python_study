#-- coding: utf-8 --
#@Time : 2021/3/9 10:32
#@Author : XXXX
#@Email : XXXX@qq.com
#@File : shuru11.py
#@Software: PyCharm
'''
输入描述:
输入有多组测试用例，每组空格隔开两个整数
输出描述:
对于每组数据输出一行两个整数的和
示例1
输入
复制
1 1
输出
复制
2
'''
while True:
    try:
        a=list(map(int,input().split()))
        print(sum(a))
    except:break