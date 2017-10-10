# -*-coding:utf-8 -*-
# Author:周健伟
#import getpass
real_username="周健伟"
real_password="123456"
username=input("username:")
#password=getpass.getpass("password:")
password=input("password:")
"""
getpass模块在pycharm中不可以显示，在cmd中运行
getpass可以将密码不可见的输入
"""
if username==real_username and password==real_password:
    print("welcome %s login....." %(username))
else:
    print("Invalid username...")