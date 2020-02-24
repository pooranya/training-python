from math import factorial as fac

def less(a,x):
    c = 0
    for i in range(len(a)):
        if a[i]<x:
            c+=1
    #print("c",c)
    return c

def rep(a):
    z = a.copy()
    z = list(set(z))
    m = 1
    for i in range(len(z)):
        m = m*fac(a.count(z[i]))
    #print("m",m)
    return m
n = list(input())
k = n.copy()
k.sort()
m = []
l = []
p = []
c = 1

for i in range(len(k)):
    if k[i] not in m:
        m.append(k[i])
        l.append(c)
        c+=1
    else:
        l.append(c)
for i in range(len(n)):
    p.append(l[k.index(n[i])])
sum = 0
f = len(p)-1
#print(p)
for i in range(len(p)-1):
    sum = sum + (less(p[i+1:],p[i])*fac(f))//rep(n[i:])
    #print(sum)
    f-=1
print(sum+1)
