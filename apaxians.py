s = raw_input()
l = []
tmp = ""
i = 0
for i in s:
    if i != tmp:
        l.append(i)
    tmp = i
string = ""
for i in l:
    string += i
print string

