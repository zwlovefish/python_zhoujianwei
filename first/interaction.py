# -*-coding:utf-8 -*-
# Author:周健伟
name=input("name:")
age=int(input("age:"))
job=input("job:")
salary=input("salary:")
info="""
----------info of %s---------
name:%s
age:%d
job:%s
salary:%s
""" %(name,name,age,job,salary)
print(info)

info2="""
-----------info of {name2}--------------
Name:{name2}
Age:{age2}
Job:{job2}
Salary:{salary2}
""".format(name2=name,
           age2=age,
           job2=job,
           salary2=salary)
print(info2)

info3="""
--------info of {0}---------
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
""".format(name,age,job,salary)
print(info3)