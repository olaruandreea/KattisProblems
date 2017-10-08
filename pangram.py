import string
n = input()
alphabet = set(string.ascii_lowercase)
i = 0 
lista = []
while i < n:
    s = raw_input()
    lista.append(s)
    i+=1
i = 0 
new = []
while i < len(lista):
    tmp = ""
    for each in lista[i]:
        if each.isalpha():
            tmp += each
    
    new.append(tmp) 
    i+=1
output = []
for every in new:
    string = ""
    if sorted(set(every.lower())) == sorted(alphabet):
        output.append("pangram")
    else:
        for i in sorted(alphabet):
            if i not in sorted(set(every.lower())):
                string += i
        output.append("missing " + string)
for i in output:
    print i
