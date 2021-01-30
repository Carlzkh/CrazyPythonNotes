"""
1. 提示用户输入自己的名字、年龄、身高，并将该用户信息以 JSON 格式保存在文件中。再写一
个程序读取刚刚保存的 JSON 文件，恢复用户输入的信息。
"""
import json
name = input('姓名：')
age = int(input('年龄：'))
height = int(input('身高：'))
dict_person = {'姓名': name, '年龄': age, '身高': height}

json_person = json.dumps(dict_person).encode('utf-8')

print(type(json_person))
print(json_person.decode('unicode_escape'))

return_dict_person = json.loads(json_person)
print(type(return_dict_person))
print(return_dict_person['姓名'])


