"""
2.利用第 1题定义的 Student 类，定义 个列表保存 Student 对象作为通讯录数据 。程序
可通过 name email address 查询，如果找不到数据，则进行友好提示
"""


class Student:
    def __init__(self, name, age, gender, phone, address, email):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.address = address
        self.email = email


def query_by_name(name):
    for i in range(len(students)):
        if students[i].name == name:
            return students[i]
        else:
            pass
    return '查无此人！'


def query_by_address(address):
    for i in range(len(students)):
        if students[i].address == address:
            return students[i]
        else:
            pass
    return '查无此地址！'


def query_by_email(email):
    for i in range(len(students)):
        if students[i].email == email:
            return students[i]
        else:
            pass
    return '查无此邮箱！'


students = []

if __name__ == '__main__':
    while True:
        student_name = input('输入姓名：')
        if student_name == 'quit':
            print('学生输入完毕！')
            break
        student_age = input('输入年龄：')
        student_gender = input('输入性别：')
        student_phone = input('输入电话：')
        student_address = input('输入地址：')
        student_email = input('输入邮箱：')
        student = Student(student_name, student_age, student_gender, student_phone, student_address, student_email)
        students.append(student)

    student_searched_by_name = query_by_name('张三')
    print(student_searched_by_name.phone)
    student_searched_by_email = query_by_email('qq@qq.com')
    print(student_searched_by_email.name)
    student_searched_by_address = query_by_address('上海市桂箐路7号1号楼6楼')
    print(student_searched_by_address.age)

    print(query_by_name('张三q'))
    print(query_by_email('qqq@qq.com'))
    print(query_by_address('q上海市桂箐路7号1号楼6楼'))




