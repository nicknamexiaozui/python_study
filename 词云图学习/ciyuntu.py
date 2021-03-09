#-- coding: utf-8 --
#@Time : 2021/2/7 10:36
#@Author : XXXX
#@Email : XXXX@qq.com
#@File : ciyuntu.py
#@Software: PyCharm
from wordcloud import WordCloud
from matplotlib import pyplot as plt
import jieba
import numpy as np
import collections
from PIL import Image
list=[]
with open('file', encoding='utf-8') as f:
	data=f.read().split('\n')
	f.close()
myword=collections.Counter(data)
maak=np.array(Image.open("mask_1.png"))
#bg=np.array(Image.open("mask_1.png")) #544X960
mycloud=WordCloud(
	background_color='white',  # 设置背景颜色  默认是black
	#mask=mask_,  # 自定义蒙版
	mode='RGBA',
	mask=maak,
	max_words=500,
	font_path='simhei.ttf',  # 设置字体  显示中文
).generate_from_frequencies(myword)
plt.imshow(mycloud)
plt.axis("off")
mycloud.to_file('test.png')