import pickle
import sys
def print_lol(the_list,indent=False,level=0,fh=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level=level+1,fh=sys.stdout)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t",end='',file=fh)
            print(each_item,file=fh)
new_man=[]
try:
    with open("man_data.txt",'rb') as man_file:
        new_man=pickle.load(man_file)
except IOError as err:
    print('File Error'+str(err))
except pickle.PickleError as perr:
    print('Pickling error'+str(perr))
try:
    with open("other_data.txt","rb") as other_file:
        other_man=pickle.load(other_file)
except IOError as err:
    print('File Error'+str(err))
except pickle.PickleError as perr:
    print('Picking error'+str(perr))
print_lol(new_man)
print('================================================================')
print_lol(other_man)
