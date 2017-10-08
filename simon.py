n = input()
i = 1 
l = []
while i <= n:
    s = raw_input()
    tokens = s.split()
    if tokens[0] == "Simon" and tokens[1] == "says":
        l.append(tokens[2:])
    i+=1

for i in l:
    new = ""
    for t in i:
        new += t + " "
    print " " + new
