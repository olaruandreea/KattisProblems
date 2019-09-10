n = input()
i = 0
while i < int(n):
    s = raw_input()
    if s[0:11] == "simon says ":
      print s[11:]
    else:
      print ""
    i+=1

