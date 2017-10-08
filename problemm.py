import sys
lines = sys.stdin.readlines()
l = []
i = 0
while i < len(lines):
    if "problem" in lines[i].lower():
        l.append("yes")
    else:
        l.append("no")   
    i = i + 1
for i in l:
    print i
