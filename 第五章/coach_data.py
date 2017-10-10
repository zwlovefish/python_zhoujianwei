def fun(the_list,file):
    try:
        data=open(file)
        try:
            line=data.readline().strip()
            line_data=line.split(',')
            the_list=line_data
        except ValueError:
            pass
    except IOError as err:
        print('File Error'+str(err))
    finally:
        data.close()
    return the_list
james_data=[]
julie_data=[]
mikey_data=[]
sarah_data=[]
clean_james=[]
clean_julie=[]
clean_mikey=[]
clean_sarah=[]
james_data=fun(james_data,"james.txt")
julie_data=fun(julie_data,"julie.txt")
mikey_data=fun(mikey_data,"mikey.txt")
sarah_data=fun(sarah_data,"sarah.txt")
###################
#james_data.sort()
#julie_data.sort()
#mikey_data.sort()
#sarah_data.sort()
#这里是原地排序，原来的数据会丢失
##################


#############################
#这里是复制排序
#print("james的数据是：")
#print(sorted(james_data))
#print("julie的数据是")
#print(sorted(julie_data))
#print("mikey的数据是")
#print(sorted(mikey_data))
#print("sarah的数据是")
#print(sorted(sarah_data))


#将一个字符串中的'-',':'变为'.'
def sanitize(time_string):
    if '-' in time_string:
        splitter='-'
    elif ':' in time_string:
        splitter=':'
    else:
        return time_string
    (mins,secs)=time_string.split(splitter)
    return (mins+"."+secs)


#处理选手数据列表中的每一项
#for eachitem in james_data:
#    clean_james.append(sanitize(eachitem))
#for eachitem in julie_data:
#    clean_julie.append(sanitize(eachitem))
#for eachitem in mikey_data:
#    clean_mikey.append(sanitize(eachitem))
#for eachitem in sarah_data:
#    clean_sarah.append(sanitize(eachitem))


#除此之外，还可以使用列表推倒
clean_james=[float(sanitize(eachitem)) for eachitem in james_data]
clean_julie=[float(sanitize(eachitem)) for eachitem in julie_data]
clean_mikey=[float(sanitize(eachitem)) for eachitem in mikey_data]
clean_sarah=[float(sanitize(eachitem)) for eachitem in sarah_data]

#打印数据
print("james的数据是：")
print(sorted(clean_james))
print("julie的数据是")
print(sorted(clean_julie))
print("mikey的数据是")
print(sorted(clean_mikey))
print("sarah的数据是")
print(sorted(clean_sarah))
