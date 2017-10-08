take = raw_input()
integers = take.split()
x = int(integers[0])
y = int(integers[1])
n = int(integers[2])
i = 1 
while i <= n:
    if i % x == 0 and i % y != 0:
        print "Fizz"
    elif i % x != 0 and i % y == 0:
        print "Buzz"
    elif i % x == 0 and i % y == 0:
        print "FizzBuzz"
    else:
        print i 
    i+=1
