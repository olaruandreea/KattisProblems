no = raw_input()
tokens = no.split()
a = int(tokens[0])
b = int(tokens[1])
c = int(tokens[2])
if a + b == c:
    print str(a) + "+" + str(b) + "=" + str(c)
elif a - b == c:
    print str(a) + "-" + str(b) + "=" + str(c)
elif a * b == c:
    print str(a) + "*" + str(b) + "=" + str(c)
elif a / b == c:
    print str(a) + "/" + str(b) + "=" + str(c)

elif a == b /c :
    print str(a) + "=" + str(b) + "/" + str(c)
elif a == b*c :
    print str(a) + "=" + str(b) + "*" + str(c)
elif a == b - c :
    print str(a) + "=" + str(b) + "-" + str(c)
elif a == b + c :
    print str(a) + "=" + str(b) + "+" + str(c)

