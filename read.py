l = []
import sys

for line in sys.stdin.readlines():
    tokens = line.split()
    l.append(int(tokens[0]) - int(tokens[1]))
for i in l:
    print abs(i)
