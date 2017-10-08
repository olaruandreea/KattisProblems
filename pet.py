i = 1
total = 0
lista = []
while i <= 5:
    s = raw_input()
    tokens = s.split()
    total =  int(tokens[0]) + int(tokens[1]) + int(tokens[2]) + int(tokens[3])
    lista.append(total)
    i+=1
i = 0 
j = 0 
maximum = 0 
while i < len(lista):
    if lista[i] > maximum:
        j = i
        maximum = lista[i]
    i+=1
print str(int(j)+1) + " " + str(maximum)
