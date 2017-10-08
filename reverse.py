n = input()
i  = 0 
lista = []
new = n
while new != 0:
    output = new % 2
    new = (new / 2) 
    
    lista.append(output)
i=0
dec = 0 
j = len(lista)-1
while i < len(lista):

    dec += (lista[i] * (2 ** j))
    i+=1
    j-=1
print dec
