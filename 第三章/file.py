man=[]
other=[]
try:
	data=open("sketch.txt")
	for each_line in data:
		try:
			(role,line_spoken)=each_line.split(":",1)
			line_spoken=line_spoken.strip()
			if role == 'Man':
				man.append(line_spoken)
			elif role == 'Other Man':
				other.append(line_spoken)
		except ValueError:
			pass
	data.close()
except IOError:
	print("文件没有找着，很尴尬")
print(man)
print(other)
