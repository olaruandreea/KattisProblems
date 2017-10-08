n = raw_input()
tokens = n.split()
first = int(tokens[0])
second = tokens[1]
lista = []
i = 1 
while i <= (first*4):
    s = raw_input()
    lista.append(s)
    i+=1
count = 0

for i in lista:
    if i[1:2] == second and i[0:1] == "K":
        count += 4
    elif i[1:2] != second and i[0:1] == "K":
        count += 4

    elif i[1:2] == second and i[0:1] == "Q":
        count += 3
    elif i[1:2] != second and i[0:1] == "Q":
        count += 3

    elif i[1:2] == second and i[0:1] == "J":
        count += 20
    elif i[1:2] != second and i[0:1] == "J":
        count += 2

    elif i[1:2] == second and i[0:1] == "A":
        count += 11
    elif i[1:2] != second and i[0:1] == "A":
        count += 11

    elif i[1:2] == second and i[0:1] == "T":
        count += 10
    elif i[1:2] != second and i[0:1] == "T":
        count += 10

    elif i[1:2] == second and i[0:1] == "9":
        count += 14
    elif i[1:2] != second and i[0:1] == "9":
        count += 0
    else:
        count += 0     
print count
