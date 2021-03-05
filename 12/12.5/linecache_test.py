import linecache
import random

# 读取random模块的源文件的第3行
print(linecache.getline(random.__file__, 3))
# 读取本程序的第3行
print(linecache.getline('linecache_test.py', 2))
# 读取普通文件的第2行
print(linecache.getline('test.txt', 1))
