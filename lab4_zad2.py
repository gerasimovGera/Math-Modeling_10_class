def masiv(a):
    a = range(1, 10, 1)
    
    w=len(a)
    s=1
    for i in range(0,len(a),1):
        s=s*a[i]
    return s
print (masiv(a))
    