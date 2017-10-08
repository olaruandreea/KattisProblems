n = raw_input()
tokens = n.split()
i = 0  
output = 0
lista = []

if tokens[0] == "1":
    lista.append("0")
elif tokens[0] > "1":
    lista.append(1 - int(tokens[0]))
else:
    lista.append((int(tokens[0]) - 1)* -1)


if tokens[1] == "1":
    lista.append("0")
elif tokens[1] > "1":
    lista.append(1 - int(tokens[1]))
else:
    lista.append((int(tokens[1]) - 1)*-1)

if tokens[2] == "2":
    lista.append("0")
elif tokens[2] > "2":
    lista.append(2 - int(tokens[2]))
else:
    lista.append((int(tokens[2]) - 2)* -1)

if tokens[3] == "2":
    lista.append("0")
elif tokens[3] > "2":
    lista.append(2 - int(tokens[3]))
else:
    lista.append((int(tokens[3])-2) * -1)


if tokens[4] == "2":
    lista.append("0")
elif tokens[4] > "2":
    lista.append(2 - int(tokens[4]))
else:
    lista.append((int(tokens[4]) - 2)*-1)


if tokens[5] == "8":
    lista.append("0")
elif tokens[5] > "8":
    lista.append(8 - int(tokens[5]))
else:
    lista.append((int(tokens[5])-8)*-1)

out = ""
for i in lista:
    out += str(i) + " "
print out
