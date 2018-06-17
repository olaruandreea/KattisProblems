s = raw_input()
import sys
tokens = s.split()
parts= tokens[0]
days = tokens[1]
i=1
j=0
output = 0 
l = []
while i <= int(days):
    inp = raw_input()
    if inp not in l:
        l.append(inp)
    if len(l) == int(parts):
        output = output + i
        print output 
        sys.exit(0)
    i+=1
if len(l) != int(parts):
    print "paradox avoided"

