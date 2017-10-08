n = input()
l = []
lista = []
while n != 0:
    count = 0
    for i in str(n):
        count += int(i) 
    l.append(count)
    lista.append(n)
    n = input()
j = 0 
out = []
while j < len(l):
    p = 11
    found = False 
    while found == False:
        check = lista[j] * p
        countt = 0
        for i in str(check):
            countt += int(i)
        if countt == l[j]:
            found = True
            out.append(p)
        p+=1     
    j+=1
for i in out:
    print i
