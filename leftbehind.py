l = []
s = raw_input()
while s != "0 0":
    tokens = s.split()
    sweet_jar = int(tokens[0])
    sour_jar = int(tokens[1])
    total = int(sweet_jar) + int(sour_jar)
    if sour_jar > sweet_jar and total != 13:
        l.append("Left beehind.")
    elif sweet_jar > sour_jar and total != 13:
        l.append("To the convention.")
    elif sweet_jar == sour_jar:
        l.append("Undecided.")
    elif total == 13:
        l.append("Never speak again.")
       
    s = raw_input()
for each in l:
    print each
