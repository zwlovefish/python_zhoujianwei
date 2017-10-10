james=[]
julie=[]
mikey=[]
sarah=[]
def get_coach_data(filename):
    with open(filename) as f:
        data=f.readline().strip().split(",")
        return data
def sanitize(time_string):
        if '-' in time_string:
            spilitter='-'
        elif ':' in time_string:
            spilitter=':'
        else:
            return time_string
        (mins,secs)=time_string.split(spilitter)
        return (mins+'.'+secs)
james=get_coach_data("james.txt")
julie=get_coach_data("julie.txt")
mikey=get_coach_data("mikey.txt")
sarah=get_coach_data("sarah.txt")
james=sorted(set([sanitize(t) for t in james]))[0:3]
julie=sorted(set([sanitize(t) for t in julie]))[0:3]
mikey=sorted(set([sanitize(t) for t in mikey]))[0:3]
sarah=sorted(set([sanitize(t) for t in sarah]))[0:3]
print(james)
print(julie)
print(mikey)
print(sarah)
