s = raw_input()
tokens = s.split()

output = ""

buying_power = int(tokens[0]) * 3 + int(tokens[1]) * 2 + int(tokens[2]) * 1

v = [8,5,2]
t = [6,3,0]
victory = [x for x in v if x <= buying_power]
tresure = [x for x in t if x <= buying_power]

if len(victory) >= 1:
    if victory[0] == 8:
       output += "Province or "
    elif victory[0] == 5:
       output += "Duchy or "
    elif victory[0] == 2:
       output += "Estate or "


if tresure[0] == 6:
       output += "Gold"
elif tresure[0] == 3:
   output += "Silver"
elif tresure[0] == 0:
   output += "Copper"
print(output)
