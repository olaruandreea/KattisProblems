s1 = raw_input()
s2 = raw_input()
count_a1 = 0
count_a2 = 0
for each in s1:
	if each == "a":
		count_a1 += 1
for each in s2:
	if each == "a":
		count_a2 += 1
if count_a1 < count_a2:
	print "no"
elif count_a1 >= count_a2:
	print "go"
