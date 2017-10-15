no = raw_input()
l = [] 
list_no = 0 
output = [] 
while no != "0":
    i = 0 
    while i < int(no):
        name = raw_input()
        tokens = name.split(" ")
        l.append(tokens[-1].lower())
        i+=1
    count = [x + " " + "|" + " " + str(l.count(x)) for x in set(l)]
    list_no += 1
    output.append("List " + str(list_no) + ":")
    for i in sorted(count):
        output.append(i)
    l[:] = []
    no = raw_input()
for each in output:
    print each
