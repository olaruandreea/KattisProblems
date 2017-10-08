s = raw_input()
l = []
for i in s:
    if i == "a" or i == "A":
        l.append("@")
    elif i == "b" or i == "B":
        l.append("8")
    elif i == "c" or i == "C":
        l.append("(")
    elif i == "d" or i == "D":
        l.append("|)")
    elif i == "e" or i == "E":
        l.append("3")
    elif i == "f" or i == "F":
        l.append("#")
    elif i == "g" or i == "G":
        l.append("6")
    elif i == "h" or i == "H":
        l.append("[-]")
    elif i == "i" or i == "I":
        l.append("|")
    elif i == "j" or i == "J":
        l.append("_|")
    elif i == "k" or i == "K":
        l.append("|<")
    elif i == "l" or i == "L":
        l.append("1")
    elif i == "m" or i == "M":
        l.append("[]\/[]")
    elif i == "n" or i == "N":
        l.append("[]\[]")
    elif i == "o" or i == "O":
        l.append("0")
    elif i == "p" or i == "P":
        l.append("|D")
    elif i == "q" or i == "Q":
        l.append("(,)")
    elif i == "r" or i == "R":
        l.append("|Z")
    elif i == "s" or i == "S":
        l.append("$")
    elif i == "t" or i == "T":
        l.append("']['")
    elif i == "u" or i == "U":
        l.append("|_|")
    elif i == "v" or i == "V":
        l.append("\/")
    elif i == "w" or i == "W":
        l.append("\/\/")
    elif i == "x" or i == "X":
        l.append("}{")
    elif i == "y" or i == "Y":
        l.append("`/")
    elif i == "z" or i == "Z":
        l.append("2")
    else:
        l.append(i)
new =  ""
for i in l:
    new += i 
print new

