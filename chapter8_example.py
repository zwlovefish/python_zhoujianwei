def shwomagican_names(magican_names):
    for each_name in magican_names:
        print(each_name,end=' ')
def make_great(magican_names):
    names=[]
    for each_name in magican_names:
        names.append('the Great '+each_name)
    return names
names=['周健伟','张文','雷佳近']
name=make_great(names[:])
shwomagican_names(name)
print()
shwomagican_names(names)
