import pickle
man=[]
other=[]
try:
    data=open("sketch.txt")
    for each_line in data:
        try:
            (role,line_spoken)=each_line.split(":")
            line_spoken=line_spoken.strip()
            if role=='Man':
                man.append(line_spoken)
            elif role=='Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
except IOError:
    print("file is Error")
finally:
    data.close()
try:
    with open("man_data.txt",'wb') as man_file,open("other_data.txt",'wb') as other_file:
        pickle.dump(man,man_file)
        pickle.dump(other,other_file)
except IOError as err:
    print("File Error is"+str(err))
