import math
s = raw_input()
tokens = s.split()
a = int(tokens[0])
i = int(tokens[1])
result = (math.ceil(a * (i -1) + 1))
t = ""
for i in str(result):
    if i != ".":
        t += i
    else:
        break
print t
