mega = input()  # X mega to surf the internet per month
months = input() 
i = 1
extra = mega
while i <= months:
     n  = input()
     extra += mega - n
     i+=1
print extra
