import os

# 获取当前目录
print(os.getcwd())  # G:\publish\codes\12\12.7
# 改变当前目录
os.chdir('../12.6')
# 再次获取当前目录
print(os.getcwd())  # G:\publish\codes\12\12.6


# path = 'my_dir'
# # 直接在当前目录下创建目录
# os.mkdir(path, 0o755)
# path = "abc/xyz/wawa"
# # 递归创建目录
# os.makedirs(path, 0o755)


# path = 'my_dir'
# # 直接重命名当前目录下的子目录
# os.rename(path, 'your_dir')
# path = "abc/xyz/wawa"
# # 递归重命名子目录
# os.renames(path, 'foo/bar/haha')


path = 'your_dir'
# 直接删除当前目录下的子目录
os.rmdir(path)
path = "foo/bar/haha"
# 递归删除子目录
os.removedirs(path)
