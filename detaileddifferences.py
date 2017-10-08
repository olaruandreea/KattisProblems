n = input()
i = 1 
l1 = []
l2 = []
while i <= 2 * n:
    s = raw_input()
    if i % 2 != 0:
        l1.append(s)
    else:
        l2.append(s)
    i+=1
i = 0 
string = ""
new = []
while i < len(l1):
    new.append(l1[i])
    new.append(l2[i])
    j = 0
    while j < len(l1[i]):
        if l1[i][j] == l2[i][j]:
            string += "."
        else:
            string += "*"
        j+=1

    new.append(string)
    string = ""
    i+=1
count  = 0
for i in new:
    if "*" not in i and "." not in i:
        print i
    else:
        print i
        print "\n"
   