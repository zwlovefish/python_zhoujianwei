# -*-coding:utf-8 -*-
# Author:周健伟
import time

def timmer(func):
    def deco(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        stop_time=time.time()
        print("the func run time is %s" %(stop_time-start_time))
    return deco
@timmer
def yanshi():
    time.sleep(3)
    print('in the yanshi')
@timmer
def with_canshu(name,age):
    time.sleep(1)
    print(name+"'s age is "+age)
yanshi()
with_canshu('周健伟','18')