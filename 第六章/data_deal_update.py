def get_coach_data(filename):
    try:
        with open(filename) as f:
            data=f.readline().strip().split(",")
            dict1=dict()
            dict1['Name']=data.pop(0)
            dict1['Dob']=data.pop(0)
            dict1['Time']=data
            dict1['Time']=str(sorted(set([sanitize(eachitem) for eachitem in dict1['Time']]))[0:3])
            return dict1
    except IOError as err:
        print("File Error:"+str(err))
        return None
def sanitize(time_string):
    if '-' in time_string:
        spilitter='-'
    elif ':' in time_string:
        spilitter=':'
    else:
        return time_string
    (mins,secs)=time_string.split(spilitter)
    return (mins+'.'+secs)
sarah2_dict=get_coach_data("sarah2.txt")
james2_dict=get_coach_data("james2.txt")
mikey2_dict=get_coach_data("mikey2.txt")
julie2_dict=get_coach_data("julie2.txt")
print(sarah2_dict['Name']+"'s fastest times are:"+sarah2_dict['Time'])
print(james2_dict['Name']+"'s fastest times are:"+james2_dict['Time'])
print(mikey2_dict['Name']+"'s fastest times are:"+mikey2_dict['Time'])
print(julie2_dict['Name']+"'s fastest times are:"+julie2_dict['Time'])

