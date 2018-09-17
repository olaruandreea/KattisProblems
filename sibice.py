import math
s = raw_input()
tokens = s.split()
matches_number = int(tokens[0])
box_w = int(tokens[1])
box_h = int(tokens[2])
fits = math.sqrt((box_w *box_w)+(box_h*box_h))
i = 0 
while i < matches_number:
    n = int(input())
    if n > fits:
        print "NE"
    else:
        print "DA"
    i+=1
