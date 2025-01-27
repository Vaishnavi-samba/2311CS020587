# converting String to list 7
#first letteer of string
# expected output : [to]
string = "welcome to the python lab"
list1 = [i for i in string.split() if len(i) == 2]
print(list1)