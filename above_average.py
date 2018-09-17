n = input()
i = 0
l = []
while i < int(n):
    s = raw_input()
    tokens = s.split()
    average = over_average = finl_average = count =  0  
    for each in tokens[1:]:
        average += int(each)
    final_average = float(average) / int(tokens[0])
    for no in tokens[1:]:
        if int(no) > final_average:
            count += 1
    l.append((count/float(tokens[0])) * 100)
    i+=1

for every_number in l:
    print ("%.3f" % every_number + "%")
