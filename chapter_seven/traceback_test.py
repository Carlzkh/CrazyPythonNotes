class SelfException(Exception):
    pass


def main():
    first_method()


def first_method():
    second_method()


def second_method():
    third_method()


def third_method():
    raise SelfException('自定义异常信息')


main()
