n = int(input())
string1 = raw_input()
string2 = raw_input()
l1 = []
l2 = []
for each in string1:
    l1.append(each)
for each in string2:
    l2.append(each)
j = 0 
while j < n:
    i = 0 
    while i < len(l1):
        if l1[i] == "1":
            l1[i] = "0"
        else:
            l1[i] = "1"
        i+=1
    j+=1
if l1 == l2:
    print "Deletion succeeded"
else:
    print "Deletion failed"
