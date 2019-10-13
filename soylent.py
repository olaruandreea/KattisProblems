import math
i = 0 
total = raw_input()
while i < int(total):
	calories  = int(raw_input())
	print int(math.ceil(calories / 400.0))
	i+=1 
