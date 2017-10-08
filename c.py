s = raw_input()
count = 0 
i = 0 
while i < len(s):
    if s[i] != "P":
        count +=1
    if s[i+1] != "E":
        count +=1
    if s[i+2] != "R":
        count +=1
    i+=3
print count
