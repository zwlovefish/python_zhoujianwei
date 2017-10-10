# -*-coding:utf-8 -*-
# Author:周健伟
User,Passwd='zhoujianwei','abc123'
def auth(auth_type):
    def out_deco(func):
        def deco(*args,**kwargs):
            if auth_type == 'local':
                username=input("username is:")
                password=input("password is:")
                if username == User and password == Passwd:
                    reg = func(*args,**kwargs)
                    print("登录成功！")
                    return reg
                else:
                    print("登录失败！")
            elif auth_type== 'ldap':
                print('搞毛线，ldap，不会啊.............')
        return deco
    return out_deco
def index():
    print('Welcome to index page')
@auth(auth_type='local')
def home():
    print('Welcome to home page')
    return 'home page'
@auth(auth_type='ldap')
def bbs():
    print('Welcome to bbs page')
index()
print(home())
bbs()