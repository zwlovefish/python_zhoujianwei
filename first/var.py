# -*-coding:utf-8 -*-
# Author:周健伟
name="周健伟"
name2=name
print(name,name2)

#name指向的是周健伟，name2通过name指向的也是周健伟，
#改变name的值，不会改变name2的值
name="李四"
print(name,name2)

