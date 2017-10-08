s = raw_input()
tokens = s.split()
hour = int(tokens[0])
sec = int(tokens[1])
sec += 15
if sec / 60 == 0:
    hour = hour - 1
else:
    sec = sec % 60
if hour < 0:
    hour += 24

print str(hour) + " " + str(sec)
