import itertools
n = int(input())
l = itertools.permutations(str(n))
lista = [int(''.join(x)) for x in l]
new = []
for i in lista:
    if i > n:
        new.append(i)
if len(new) == 0:
    print 0
else:
    print min(new)
