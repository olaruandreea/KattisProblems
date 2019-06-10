import decimal
n = float(input())
output = (1000*1.08776267)
a = decimal.Decimal(output*n)
out = (round(a,0))
print str(out)[0:-2]
