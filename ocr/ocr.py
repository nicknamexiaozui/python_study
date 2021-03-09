#-- coding: utf-8 --
#@Time : 2021/2/24 15:32
#@Author : XXXX
#@Email : XXXX@qq.com
#@File : ocr.py
#@Software: PyCharm
from selenium import webdriver
import re
from time import sleep
driver= webdriver.Firefox()
driver.get('https://gs.whu.edu.cn/tzgg/zs.htm')
for i in range(0,25):
	id='line_u4_'+str(i)
	a = driver.find_element_by_id(id).text
	with open('result.txt','a',encoding='utf-8')as f:
		f.write('第***1***页，第'+str(i+1)+'条'+a+'\n')
yeshu=1
for y in range(2,10):
	driver.find_element_by_link_text('下页').click()
	yeshu=yeshu+1
	tiaoshu = 0
	for w in range(15, 40):
		tiaoshu = tiaoshu + 1
		id = 'line_u4_' + str(w)
		a = driver.find_element_by_id(id).text
		with open('result.txt', 'a', encoding='utf-8')as f:
			f.write('第***'+str(yeshu)+'***页，第' + str(tiaoshu) + '条' + a + '\n')
driver.find_element_by_link_text('下页').click()
x=0
for i in range(15,25):
	x=x+1
	id='line_u4_'+str(i)
	a = driver.find_element_by_id(id).text
	with open('result.txt','a',encoding='utf-8')as f:
		f.write('第***10***页，第'+str(x)+'条'+a+'\n')
# # print(txt)
# a = driver.page_source
# print(a)
# a=driver.page_source
# # print(a)
# # print(type(a))
# txt=re.findall("htm\">(.*?)</a></li>", a)
# print(txt)
