
def visokos(a):
    if a%400==0 or (a%100!=0 and a%4==0):
        return('високосный')
    else:
        return('невисокочный')       
print(visokos(2100))