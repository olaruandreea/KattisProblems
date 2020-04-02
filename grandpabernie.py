def createDictionary():
	n = input()
	i = 0 
	d = {}
	while i < n:
		tokens = raw_input().split()
		if tokens[0] not in d:
			d[tokens[0]] = [tokens[1]]
		else:
			d[tokens[0]].append(tokens[1])
		i+=1
	n2 = input()
	i = 0 
	l = []
	while i < n2:
		tokens = raw_input().split()
		l.append(sorted(d[tokens[0]])[int(tokens[1])-1])
		i+=1
	return "\n".join(l)

print createDictionary()
