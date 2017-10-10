# Author:周健伟
# 每个用户登录三次，登录成功
#则显示欢迎登录，三次登录失败则
#将该用户锁定。将登录用户从文件中读出，
#锁起来的用户也保存在文件中
def login(filename):
    userName = []
    passWord = []
    try:
        data = open(filename)
        for each_line in data:
            (username,password)=each_line.strip().split(",")
            userName.append(username)
            passWord.append(password)
        can_login = {}
        for i in range(0, len(userName)):
            can_login[userName[i]] = passWord[i]
        return can_login
    except IOError as err:
        print("File open error")
    finally:
        data.close()
def lock(filename,username):
    try:
        data=open(filename,'a')
        data.write("\n"+username)
    except IOError as error:
        print("写入文件失败")
    finally:
        data.close()
def get_lock_name(filename):
    lockname=[]
    data=open(filename)
    for each_line in data:
        lockname.append(each_line.strip())
    return lockname
login_user_passwd=login("username_and_passwd.txt")
count=0
while count < 3:
    temp_username=input("请输入用户名：")
    temp_password=input("请输入密  码：")
    if temp_username in get_lock_name("lockusername.txt"):
        print("你输入的用户已被锁定...")
        break
    if temp_username in login_user_passwd.keys():
        if login_user_passwd[temp_username]==temp_password :
            print("welcome ",temp_username)
            break
        else:
            print("sorry,your username or password is not true...")
    else:
        print("your username does not exist")
    count += 1
else:
    lock("lockusername.txt",temp_username)
    print("your username is locked....")