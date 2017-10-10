def fun(x) :
    if x==1:
        return 1
    else:
        return fun(x-1)*x
x=int(input("请输入一个数"))
print(fun(x))
