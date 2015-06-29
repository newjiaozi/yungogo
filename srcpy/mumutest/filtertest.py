# _*_  coding: utf-8  _*_
# 编码格式utf-8
'''
Created on 2015年6月29日 -下午4:09:59

@author:  Jz
'''

a = range(1,101)
def suShu(arg1):                # 判断arg1是否为素数，是返回True
    if arg1 in (1,2):           # 不是则返回False
        pass
    else:
        for i in range(2,arg1): # 用arg1对从2，到arg1-1的数值就行除法
            if(arg1 % i == 0):  # 如果又能够取余为0，说明不是素数
                return False    # 返回False
    print arg1                  # 剩余的都是素数
    return True                 # 素数返回True
            
if __name__ == '__main__':
    filter(suShu,a)             # 使用filter过滤出a列表中是素数的数