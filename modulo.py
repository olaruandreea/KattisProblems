i = 0 
lista = []
while i < 10:
    n = input()
    lista.append(n)
    i+=1
l = []
for i in lista:
    check =  int(i) % 42
    if check not in l:
        l.append(check)
count = 0 
for i in l:
    count += 1
print count
