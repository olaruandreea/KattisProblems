temperature = input()
no = raw_input()
tokens = no.split()
count = 0 
for i in tokens:
    if int(i) < 0:
        count +=1
print count
