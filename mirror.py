number = int(input())
i = 0 
j = 0 
list1 = []
newlist = [] 
while i < number:
    token = raw_input().split()[0]
    j = 0 
    while j < int(token):
        read = raw_input()
        list1.append(read[::-1])
        j+=1
    list1.append('Test ' + str(i+1))
    newlist.append(list1[::-1])
    list1[:] = []
    i+=1
for each in newlist:
    for every in each:
        print every
