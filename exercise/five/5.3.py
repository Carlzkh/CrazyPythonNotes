"""
3. 定义一个 is leap(year 函数，该函数可判断 year 是否为闰年。若是闰年，则返回 True ；否
则返回 False
"""


def is_leap(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        else:
            if year % 400 == 0:
                return True
            else:
                return False
    else:
        return False


print(is_leap(1900))
print(is_leap(2000))
print(is_leap(2001))
print(is_leap(2004))
