s = raw_input()
tokens = s.split()
first = tokens[0]
second = tokens[1]
new1 = first[::-1]
new2 = second[::-1]

if int(new1) > int(new2):
    print new1
else:
    print new2 
