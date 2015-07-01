# _*_  coding: utf-8  _*_
# 编码格式utf-8
'''
Created on 2015年7月1日 -上午11:33:16

@author:  Jz
'''
def log(*arg1):
    def wrap1(func):
        def wrapper():
            print '--- %s %s ---' % (arg1,func.__name__)
            return func()
        return wrapper
    return wrap1

@log
def f1():
    print "f1"

@log("OOOOO")
def f2():
    print "f2"
if __name__ == '__main__':
#    f1()
    print "*"*20
    f2()