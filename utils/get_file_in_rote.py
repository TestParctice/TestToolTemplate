# encoding:utf-8
"""
@Software:PyCharm
@Time:2022/12/5 16:35
@Author:yzx
"""
import os


def file(path):
    file_list = []
    for dir in os.listdir(path):
        if (os.path.isdir(path + '/' + dir)):
            if (dir[0] == '.'):
                pass
            else:
                file_list.append(dir)
    # file_list.remove('__pycache__')
    print(len(file_list))
    print(file_list)
    return file_list


if __name__ == '__main__':
    file('D:\\workspace\\pycharmSpaces\\TestToolTemplate1\\TestToolTemplate')
    # file('/Users/PycharmProjects/Test/Peppa/testcase')
