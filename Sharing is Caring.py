def g(c,d):
    if(d!=0):
        return g(d,c%d)
    else:
        return c
a,b=map(int,input().split())
print(g(a-b,b))
