"""
3. 实现一个程序，该程序提示用户输入 个文件路径，程序读取这个可能包含手机号码的文
本文件（该文件内容可能很大），要求程序能识别出该文本文件中所有的手机号码，并将这些手机
号码保存到 phone.txt 件中
"""
from pathlib import *
import re
import os
import sys
import codecs


phone_pattern = r'1[358]\d{9}|14[579]\d{8}|16[6]\d{8}|17[0135678]\d{8}|19[89]\d{8}'

dir_str = input('请输入文件路径: ').strip()
p = Path(dir_str)
if not p.exists() or not p.is_file():
    raise ValueError('您输入的不是有效的文件')


class IdentifyErro:
    pass


def read_phones(rf1, wf1):
    while True:
        line = f.readline()
        # 如果没有读到数据，跳出循环
        if not line:
            break
        phone_list = re.findall(phone_pattern, line)
        for x in phone_list:
            wf.write(x + os.linesep)
    f.close()


with open('phone.txt', 'w+') as wf:
    # 目标文件内容可能很大，故逐行读取，尝试用gbk或utf-8两种字符集读取
    try:
        f = codecs.open(dir_str, 'r', 'gbk', buffering=True)
        read_phones(f, wf)
    except IdentifyErro as e:
        try:
            f = codecs.open(dir_str, 'r', 'utf-8', buffering=True)
            read_phones(f, wf)
        except IdentifyErro as e:
            print('该文件不是文本文件')
            sys.exit(0)
