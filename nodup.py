phrase = raw_input()
l = []
tokens = phrase.split()
for each in tokens:
    if each not in l:
        l.append(each)
if " ".join(l) == phrase:
    print "yes"
else:
    print "no"
