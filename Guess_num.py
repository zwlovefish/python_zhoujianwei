import random
status=True
while status:
    temp=input("请猜猜哥现在想的数字是什么？")
    Guess=int(temp)
    secret=random.randint(1,50)
    while Guess != secret:
        if Guess > secret:
            print("哥们，你猜的大了")
        else:
            print("哥们，你猜的小了")
        Guess=int(input("再来猜猜："))
    print("牛逼，这都能猜到，可是猜到了又有什么用呢")
    stop=input("你还想在玩吗？y/n")
    if stop == 'y':
        status=True
    else:
        status=False
print("Game Over")
