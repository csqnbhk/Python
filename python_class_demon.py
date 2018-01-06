"""
author:demon
time : 2018/1/6
python_class_demon.py :简单测试python的类

"""


class Student:
    Flag = 1

    # 初始化(可以认为是构造函数，可以在里面定义一些变量）
    def __init__(self, name, idnum):
        self.name = name
        self.idnum = idnum

    # 实例方法
    def info(self):
        print('name:{},idnum:{}'.format(self.name, self.idnum))

    # 静态方法
    @staticmethod
    def static_method():
        print('这是类的静态方法定义')

    # 类方法
    @classmethod
    def class_method(cls):
        print('这是类方法定义')


def main():
    obj = Student('demon', 2018001)
    # 调用实例方法，使用obj实例对象.方法 调用
    obj.info()
    # 调用静态方法，使用Student类.方法 调用
    Student.static_method()
    # 调用类方法，使用 Student类.方法 调用
    Student.class_method()


if __name__ == '__main__':
    main()
