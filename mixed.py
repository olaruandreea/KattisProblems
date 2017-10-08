s = raw_input()
out1 = 0
out2 = 0
l = []
while s != "0 0":
    tokens = s.split()
    if int(tokens[0]) < int(tokens[1]):
        l.append("0 " + tokens[0] + " / " + tokens[1])
    elif int(tokens[0]) >= int(tokens[1]):
        out1 = int(tokens[0]) / int(tokens[1])
        out2 = int(tokens[0]) % int(tokens[1])
        l.append(str(out1) + " " + str(out2) + " / " + str(tokens[1]))
    s = raw_input()
i = 0 
string = ""
while i < len(l):
    string = l[i]
    print string
    i+=1

