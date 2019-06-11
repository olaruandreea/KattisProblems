n1 = int(input())
n2 = raw_input()
expenses = 0
for each in n2.split():
    if each.startswith("-"):
        expenses += int(each)
if expenses == 0:
    print "0"
else:
    print str(expenses)[1:]

