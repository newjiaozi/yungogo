# _*_  coding: utf-8  _*_
# 编码格式utf-8
'''
Created on 2015年7月1日 -上午11:05:09

@author:  Jz
'''

import functools
def decorator2(func):
    @functools.wraps(func)
    def tt():
        print '--- %s -- %s' % ('Begin call',func.__name__)
        return func()
    return tt

@decorator2
def f1():
    print 'running f1'
    print '--- %s -- %s' % ('End call',f1.__name__)
if __name__ == '__main__':
    f1()