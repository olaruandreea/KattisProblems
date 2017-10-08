n = input()
i = 0 
lista = []
while i < n:
    new  =  input()
    lista.append(new)
    i+=1
output = 0
for i in lista:
    first = str(i)[:-1]
    second = str(i)[-1]
    output += int(first) ** int(second) 
print output
