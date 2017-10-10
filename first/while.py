# -*-coding:utf-8 -*-
# Author:周健伟
number=68
count=0
while count<3:
    Guess=int(input("Guess Number is :"))
    if Guess == number:
        print("You got it....")
        break
    elif Guess <number:
        print("Think bigger......")
    else:
        print("Think smaller.......")
    count += 1
else:
    # 在上面的while内的程序正常走完时执行此程序
    # for循环也可以使用这个else语句
    print("You have tried too many times....")