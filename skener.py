n = raw_input()
tokens = n.split()
R = int(tokens[0])
C = int(tokens[1])
Zr = int(tokens[2])
Zc = int(tokens[3])
new = []
i = 0  
lista = []
while i < R:
  raws = raw_input()
  for each in range(Zr):
     lista = [K * Zc for K in raws]
     print("".join(lista))
  i = i + 1


