#find if thr length of the string is even print as even
string = "do what i say to world"
for word in string.split():
  if len(word) % 1 == 0:
    print(word)
# find the length of the string if the length of the string is