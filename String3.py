# convert string to list & first letter of string
string = "do what i say to world"
for word in string.split():
  if len(word) > 3:
    print(word[0])