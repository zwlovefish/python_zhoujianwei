#使用用户输入来填充字典
mountains={}
polling_active=True
while polling_active :
    name=input('请输入名字：')
    response=input('请输入你想要爬的山')
    mountains[name]=response
    repeat=input("你还想要继续输入啊？yes/no")
    if repeat=='no':
        polling_active=False

print("结果是：")
for name,mountain in mountains.items():
    print(name+' 喜欢爬 '+mountain)
