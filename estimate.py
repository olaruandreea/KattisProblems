n = input()
i = 0 
lista = []
while i < n:
    number = raw_input()
    count = 0 
    j = 0 
    while j < len(number):
        count += 1
        j+=1
    lista.append(count)
    i+=1
for i in lista:
    print i
