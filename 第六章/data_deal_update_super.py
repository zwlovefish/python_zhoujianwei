class Athlete:
    def __init__(self,name,dob=None,times=[]):
        self.name=name
        self.dob=dob
        self.times=times
    def top3(self):
        return sorted(set([sanitize(eachitem) for eachitem in self.times]))[0:3]
    def add_time(self,time_value):
        self.times.append(time_value)
    def add_times(self,list_time_value):
        self.times.extend(list_time_value)
        
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data=f.readline().strip().split(",")
            role=Athlete(data.pop(0),data.pop(0),data)
            return role
    except IOError as err:
        print("File Error:"+str(err))
        return None
    
def sanitize(time_string):
    if '-' in time_string:
        splitter='-'
    elif ':' in time_string:
        splitter=':'
    else:
        return time_string
    (mins,secs)=time_string.split(splitter)
    return (mins+"."+secs)

james=get_coach_data("james2.txt")
julie=get_coach_data('julie2.txt')
mikey=get_coach_data('mikey2.txt')
sarah=get_coach_data('sarah2.txt')
print(james.name+"'s fastest times are:"+str(james.top3()))
print(julie.name+"'s fastest times are:"+str(julie.top3()))
print(mikey.name+"'s fastest times are:"+str(mikey.top3()))
print(sarah.name+"'s fastest times are:"+str(sarah.top3()))

        
    
