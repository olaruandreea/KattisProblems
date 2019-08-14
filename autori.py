names = raw_input()
tokens = names.split("-")
output =""
for name in tokens:
    output += name[0]
print output
