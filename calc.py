p = int(input("enter principal amount"))
r = int(input("enter rate of interest"))
t = int(input("enter time period"))
amount = p*(1+r/100)**t
print(amount)