#-- coding: utf-8 --
#@Time : 2021/3/2 14:59
#@Author : XXXX
#@Email : XXXX@qq.com
#@File : te.py
#@Software: PyCharm
from selenium import webdriver
import re
from time import sleep
driver= webdriver.Firefox()
driver.get('https://gs.whu.edu.cn/tzgg/zs.htm')
for i in range(0,1):
	id='line_u4_'+str(i)
	a = driver.find_element_by_id(id).text
	result='初试成绩查询'in a
	print(result)
	b=a.replace('\n','')
	print(b)
	b=b[12:]+b[:12]
	print(b)
	# c=b[:12]
	# print(c)
	# d=b[12:]
	# print(d)