import sys
Set = set()
l = []
for line in sys.stdin:
    tokens = line.split()
    out_line = []
    for each in tokens:
        if each.upper() in Set:
            out_line.append(".")
        else:
            out_line.append(each)
            Set.add(each.upper())
    l.append(out_line)
for xs in l:
     print(" ".join(map(str, xs)))
