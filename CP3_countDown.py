# -*- coding:utf-8 -*-
def countDown(i):
    print('\n',i)
    if i <= 0:  # 基线条件
        return
    else:       # 递归条件
        countDown(i=i-1)

countDown(3)
