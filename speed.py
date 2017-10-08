l = []
n = input()
while n != -1:
    i = 0
    tmp = 0  
    out = 0 
    while i < n:
        s = raw_input()
        tokens = s.split()
        out += (int(tokens[1]) - tmp) * int(tokens[0])
        tmp = int(tokens[1])
        i+=1
    l.append(out)
    n = input()
for i in l:
    print str(i) + " miles"

