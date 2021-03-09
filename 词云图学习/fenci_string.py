#-- coding: utf-8 --
#@Time : 2021/2/7 14:24
#@Author : XXXX
#@Email : XXXX@qq.com
#@File : fenci_string.py
#@Software: PyCharm
'''
分词统计的对象是一串长字符串，dict.txt为自定义词库
'''
import jieba
import os
import collections
class Fenci_string():
	def fenci_string(self,file,dict='./dict.txt'):
		with open(file, encoding='utf-8') as f:
			data = f.read()
			f.close()
		if not os.path.exists(dict):  # 判断文件是否存在,不存在则创建
			fd = open(dict, mode="w", encoding="utf-8")
			fd.close()
		jieba.load_userdict(dict)
		newdata="|".join(jieba.cut(data))
		myword = collections.Counter(newdata.split('|'))#以“|”为分割节点，分割的数据写进列表中
		return myword
if __name__ == '__main__':
	a=Fenci_string()
	b=a.fenci_string('./test','./dict')
	print(b)