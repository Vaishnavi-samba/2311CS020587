#find if the length of the string is even print as even
string = "do what i say to world"
for word in string.split():
  if len(word) % 2 == 0:
    print(word)