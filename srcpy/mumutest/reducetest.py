# _*_  coding: utf-8  _*_
# 编码格式utf-8
'''
Created on 2015年6月29日 -下午4:01:40

@author:  Jz
'''
a = [1,4,6,7,8]
def prod():
    b = reduce(lambda x,y:x*y,a)
    print b
if __name__ == '__main__':
    prod()