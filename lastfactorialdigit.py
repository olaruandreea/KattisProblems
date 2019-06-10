n = int(input())
i = 0
l = []
def recur_factorial(n):
   """Function to return the factorial
   of a number using recursion"""
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

while i < n:
    s = int(input())
    factorial = recur_factorial(s)
    l.append(str(factorial)[-1])
    i+=1

for i in l:
    print (i)
