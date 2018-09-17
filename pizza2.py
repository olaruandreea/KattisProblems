import math
s = raw_input()
tokens = s.split()
r = int(tokens[0])
c = int(tokens[1])
pizza = math.pi * r ** 2
cheese = math.pi * (r - c) ** 2
percent = (cheese / pizza) * 100
print(percent)
