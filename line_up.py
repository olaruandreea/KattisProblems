n = input()
i = 0 
l = [] 
while i < n:
    s = raw_input()
    l.append(s)
    i+=1

new = sorted(l)
if l == new:
    print "INCREASING"
elif l == new[::-1]:
    print "DECREASING"
else:
    print "NEITHER"
