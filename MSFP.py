import hashlib
password = raw_input()
password2 = list(password)
dict = {}
dictionary = open("C:\Users\Student\Desktop\dictionary.txt", "r")
for line in dictionary:
    passhash = hashlib.md5(b'' + line)
    #print(passhash.hexdigest())
    dict[passhash] = line
print("done")

