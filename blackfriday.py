no = raw_input()
numbers = raw_input()
l = []
take = numbers.split(" ")
for i in take:
    l.append(i)
newlist = [] 
for i in l:
    if l.count(i) == 1:
        newlist.append(i)
if len(newlist) == 0:
    print "none"
else:
    maximum = max(newlist)
    print l.index(maximum)+1
