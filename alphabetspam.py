line = raw_input()
whitespace = lowercase = uppercase = symbols = 0 
for each in line:
    if each.islower():
        lowercase += 1
    elif each.isupper():
        uppercase += 1
    elif each == "_":
        whitespace += 1 
    else:
        symbols += 1
total = float(len(line))
print float(whitespace) / total 
print float(lowercase) / total
print float(uppercase) / total 
print float(symbols) / total

