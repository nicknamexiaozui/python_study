#-- coding: utf-8 --
#@Time : 2021/2/7 14:23
#@Author : XXXX
#@Email : XXXX@qq.com
#@File : fenci_list.py
#@Software: PyCharm
'''
分词统计的对象自带换行形式
'''
import collections
class Fenci_list():
	def fenci(self,file):
		with open(file, encoding='utf-8') as f:
			data = f.read().split('\n')
			f.close()
		mycounter=collections.Counter(data)
		return mycounter
if __name__ == '__main__':
	fenci=Fenci_list()
	a=fenci.fenci('./file')
	print(a)