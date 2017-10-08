n = input()
i = 0 
while i <= n:
    if i % 2 == 0:
        winner = "Bob"
    else:
        winner = "Alice"
    i+=1
print winner
