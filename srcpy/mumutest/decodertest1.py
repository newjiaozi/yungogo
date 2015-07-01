# _*_  coding: utf-8  _*_
# 编码格式utf-8
'''
Created on 2015年7月1日 -上午10:40:39

@author:  Jz
'''
def decorator2(text):
    def logs(func):
        def wrapped(*args,**dicts):
            print '---- %s,%s' % (text,func.__name__)
            return func(*args,**dicts)
        return wrapped
    return logs

@decorator2('*****')
def u():
    print 'ooo'
if __name__ == '__main__':
    u()
    print u.__name__
