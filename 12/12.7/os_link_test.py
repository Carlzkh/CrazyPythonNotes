import os

# 为os.link_test.py文件创建快捷方式
os.symlink('os.link_test.py', 'tt')
# 为os.link_test.py文件创建硬连接（Windows上就是复制文件）
os.link('os.link_test.py', 'dst')
