i = 0
l = []
n = int(input())
while i < n:
    s = raw_input()
    tokens = s.split()
    if (int(tokens[0]) + int(tokens[1]) == int(tokens[2])) or (int(tokens[0]) - int(tokens[1]) == int(tokens[2])) or (int(tokens[1]) - int(tokens[0]) == int(tokens[2])) or (int(tokens[0]) * int(tokens[1]) == int(tokens[2])) or (int(tokens[2]) * int(tokens[1]) == int(tokens[0])) or (int(tokens[2]) * int(tokens[0]) == int(tokens[1])):
        print "Possible"
    else:
        print "Impossible"
    i+=1
