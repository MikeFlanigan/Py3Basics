'''
JSON is a widely readable file writing system both by humans and
multiple programming languages
'''
import json

#############################
## Writing
json_string = '{"first_name": "Mike", "last_name": "Flan"}'
with open('JSONtest.txt','w') as outfile: ## the w mode will over write the file
##with open('JSONtest.txt','a') as outfile: ## the a mode will append to the file
    json.dump(json_string, outfile)
outfile.close()

## Reading
with open('JSONtest.txt','r') as datafile:
    data_string = json.load(datafile)
    print("data string 1: ",data_string)
datafile.close()

## Parsing
parsed_json = json.loads(data_string)
print(parsed_json['first_name'])
##############################
############################
mylist = ['dog', 'boat', 'plane', 'robot']
with open('JSONtest2.txt','w') as outfile:
    json.dump(mylist, outfile)
outfile.close()

with open('JSONtest2.txt','r') as datafile:
    data_string = json.load(datafile)
    print("data string 2: ",data_string)
datafile.close()
############################
############################
myset = [(2,0),(4,1)]
with open('JSONtest3.txt','w') as outfile:
    json.dump(myset, outfile)
outfile.close()

with open('JSONtest3.txt','r') as datafile:
    data_string = json.load(datafile)
    print("data string 3: ",data_string)
datafile.close()
############################
############################
list1 = [1, 2,3,4,5]
list2 = [3,4,4,5,6]
dictionary = dict(zip(list1,list2))
print("dictionary 1: ", dictionary)
pos_list = [(2,0),(4,1)]
frame = [1,2]
dictionary2 = dict(zip(frame,pos_list))
print("dictionary 2: ",dictionary2)
pos_list = [(2,0),(4,1)]
frame = [1,2]
objcount = [0,1]
dictionary3 = dict(zip(objcount,dictionary2))
print("dictionary 3: ",dictionary3)

d = {} # defines d as a dictionary
d['0']={} # defines that the key '0' in dict is another dictionary
d['0']['0']= {'x':'1' , 'y':'0'}
print("d: ",d)
d_string = json.dumps(d)
d_parsed = json.loads(d_string)
print("d parsed, accessing trace 0, frame 0, x pos: ", d_parsed['0']['0']['x']," ypos: ", d_parsed['0']['0']['y'])
