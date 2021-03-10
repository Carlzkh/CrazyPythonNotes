"""
4. 实现一个程序， 该程序提示用户输入一个目录， 程序递归读取该目录及其子目录下所有能
识别的文本文件，要求程序能识别出所有文件中的所有手机号码，并将这些手机号码保存到
phones.txt 文件中
"""
from pathlib import *
import re
import os

phone_pattern = r'1[358][0-9]\d{8}|14[579]\d{8}|16[6]\d{8}|17[0135678]\d{8}|19[89]\d{8}'
f = open('phones.txt', 'w+')


def process_dir(path):
    for x in p.iterdir():
        if Path(x).is_dir():
            process_dir(Path(x))
        else:
            try:
                content = Path(x).read_text(encoding='GBK')
                phone_list = re.findall(phone_pattern, content)
                for y in phone_list:
                    f.write(y + os.linesep)
            except ValueError as e:
                try:
                    content = Path(x).read_text(encoding='GBK')
                    phone_list = re.findall(phone_pattern, content)
                    for z in phone_list:
                        f.write(z + os.linesep)
                except ValueError as e:
                    pass


dir_str = input('请输入路径: ')
p = Path(dir_str)
if not p.exists() or not p.is_dir():
    raise ValueError('您输入的不是有效的路径')
process_dir(p)
f.close()



