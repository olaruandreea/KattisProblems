n = input()
i = 0 
l = []
new = []
while i < n:
    no = input()
    j = 0 
    count = 0 
    while j < no:
        s = raw_input()
        if s not in l:
             l.append(s)
             count += 1
        j+=1
    new.append(count)
    i+=1
for i in new:
    print i 
