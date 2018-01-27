phrase = raw_input()
tokens = phrase.split(" ")
string = ""
output = []
vowels = ["a","e","i","o","u"]
for each in tokens:
    i = 0 
    while i < len(each):
        if each[i] in vowels:
            string += each[i] 
            i+=3
        else:
            string += each[i] 
            i+=1
    output.append(string)
    string = ""
print " ".join(output)
