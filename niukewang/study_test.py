#-- coding: utf-8 --
#@Time : 2021/3/9 14:45
#@Author : XXXX
#@Email : XXXX@qq.com
#@File : study_test.py
#@Software: PyCharm
def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


year = int(input("请输入年份："))

if is_leap_year(year):
    print('闰年')
else:
    print('非闰年')
#加注释