s = raw_input()
tokens = s.split()
first =int(tokens[0])
second = int(tokens[1])
if second > first:
    remainder = second - first
    if remainder == 1:
        print "Dr. Chaz will have " + str(second - first) + " piece of chicken left over!"
    else:
        print "Dr. Chaz will have " + str(second - first) + " pieces of chicken left over!" 
if first >  second:
    out = first-second
    if out == 1:
        print "Dr. Chaz needs " + str(out) + " more piece of chicken!"
    else:
        print "Dr. Chaz needs " + str(out) + " more pieces of chicken!"