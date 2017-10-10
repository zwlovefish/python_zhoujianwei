def get_coach_data(filename):
    try:
        with open(filename) as f:
            data=f.readline()
            return data.strip().split(",")
    except IOError as err:
        print("file error:"+str(error))
        return (None)
def sanitize(time_string):
    if '-' in time_string:
        spilitter='-'
    elif ':' in time_string:
        spilitter=':'
    else:
        return time_string
    (mins,secs)=time_string.split(spilitter)
    return (mins+"."+secs)
sarah=get_coach_data("sarah2.txt")
#(sarah_name,sarah_dob)=sarah.pop(0),sarah.pop(0)
#print(sarah_name+"'s fastest times are:"+str(sorted(set([sanitize(eachitem) for eachitem in sarah]))[0:3]))
sarah_data={}
sarah_data['Name']=sarah.pop(0)
sarah_data['Dob']=sarah.pop(0)
sarah_data['time']=sarah
print(sarah_data['Name']+"'s fastest time are:"+str(sorted(set([sanitize(eachitem) for eachitem in sarah_data['time']]))[0:3]))
