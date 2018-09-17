d = {
	'a': '2',
	'b': '22',
	'c': '222',
	'd': '3',
	'e': '33',
	'f': '333',
	'g': '4',
	'h': '44',
	'i': '444',
	'j': '5',
	'k': '55',
	'l': '555',
	'm': '6',
	'n': '66',
	'o': '666',
	'p': '7',
	'q': '77',
	'r': '777',
	's': '7777',
	't': '8',
	'u': '88',
	'v': '888',
	'w': '9',
	'x': '99',
	'y': '999',
	'z': '9999',
	' ': '0',
}

i = 1
n = input()
l = []
while i <= int(n):
    s = raw_input()
    string = " "
    for letter in s:
         if len(string) > 0 and string[-1] in d[letter]:
             string += " " + d[letter]
         else: 
             string += d[letter]
    l.append("Case #"+ str(i) +":" + string)
    i+=1
for each in l:
    print each


