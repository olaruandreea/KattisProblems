"""
https://open.kattis.com/problems/freefood
"""
i = 0
days = [] 
n = raw_input()
while i < int(n):
    events = raw_input()
    tokens = events.split()
    j = int(tokens[0])
    while j <= int(tokens[1]):
        if int(j) not in days:
            days.append(int(j))
        j+=1
    i+=1

print len(days)





