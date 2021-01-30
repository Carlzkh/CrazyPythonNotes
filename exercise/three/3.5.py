"""
5. 用户输入 一个整数 n，生成长度为 n的列表，将 n个随机的大写字符放入列表中


  生成一个指定长度的随机字符串，其中
  string.digits=0123456789
  string.ascii_letters=abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

  str_list = [random.choice(string.digits + string.ascii_letters) for i in range(randomlength)]
  random_str = ''.join(str_list)
"""
import random
import string

N = int(input("输入整数N："))
str_list = [random.choice(string.ascii_letters) for i in range(N)]
random_str = ''.join(str_list)
print(random_str)
print(random_str.upper())
list1 = list(random_str.upper())
print(list1)
