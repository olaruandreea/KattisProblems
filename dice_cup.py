no = raw_input()
tokens = no.split()
first = tokens[0]
second = tokens[1]
if int(first) == int(second):
    print int(first) + 1
elif int(first) < int(second):
    i = int(first) + 1 
    while i <= int(second)+ 1:
        print i 
        i+=1
else:
    i = int(second) + 1
    while i <= int(first) + 1:
        print i 
        i+=1



















































