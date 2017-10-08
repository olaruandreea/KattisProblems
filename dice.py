no1 = raw_input()
no2 = raw_input()
lista = []
count1 = 0 
tokens1 = no1.split()
count1 = 0 
for i in tokens1:
    count1 += int(i)
tokens2 = no2.split()
count2 = 0 
for i in tokens2:
    count2 += int(i)
if count1 > count2:
    print "Gunnar"
elif  count1 < count2:
    print "Emma"
else:
    print "Tie"
