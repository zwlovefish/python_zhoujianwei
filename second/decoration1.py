# -*-coding:utf-8 -*-
# Author:周健伟
#这里是高阶函数
import time
def bar():
    time.sleep(3)
    print("in tht bar")
def t_est(func):
    print(func)
    return func
bar=t_est(bar)
bar()
#这里是嵌入函数
def foo():
    print('in the foo')
    def bar1():
        print("in the bar")
    bar1()
foo()