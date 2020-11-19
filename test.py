import json
 
# print ('Number of arguments:', len(sys.argv), 'arguments.')
# print ('Argument List:', type(sys.argv))
 
 
# f = open(sys.argv[1])
# data = json.load(f)
 
my_list = [""]
path = ""
 
def recur(object, path, count):
	temppath = path
	# print(object, type(object))

	if type(object) == type(""):
		path = path + '.' + object
		return
  
	for key, value in object.items():
		if type(value) == type({}):
			stringreturned = recur(value, key+'.'+path, count+1)
			path = path + key +'.'+ stringreturned if stringreturned else "" 
 
			my_list.pop()
			my_list.append(path)
 
		elif type(value) == type([]):
			for every_dict in value:
				stringreturned = recur(every_dict, key+'.'+ path, count+1)
				path = path + key +'.'+ stringreturned if stringreturned else "" 
				my_list.pop()
				my_list.append(path) 
 
		else:
			path = path+key +'.'+ str(value)
			my_list.pop()
			my_list.append(path)
 

		path=temppath
		my_list.append('')
 
	return my_list[-1]
 
 
recur(mydata, path, 0)
 
# for i in my_list:
# 	print(i)
 
with open('output.txt', 'w') as outputfile:
    for item in my_list:
        outputfile.write("%s\n" % item)