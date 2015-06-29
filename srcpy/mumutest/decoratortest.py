# _*_  coding: utf-8  _*_
# 编码格式utf-8
'''
Created on 2015年6月29日 -下午5:41:51

@author:  Jz
'''
def log1(func):
    def wrapped(*arg,**dict1):
        print "###",func.__name__
        return func(*arg,**dict1)
    return wrapped



@log1
def now1():
    print '2015-06-29\n'   ## 相当于执行log1(now1)()
     
if __name__ == '__main__':
    now1()
    