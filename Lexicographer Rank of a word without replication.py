from math import factorial as f
def less(a,i):
    c=0
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            c+=1
    return c
n=list(input())
m=n.copy()
m.sort()
k=[m.index(n[i])+1 for i in range(len(m))]
print(k)
l=[]
l=[less(k,i) for i in range(len(k)-1)]
print(l)
g=0
x=len(n)-1
for i in l:
    g=g+i*f(x)
    x-=1
print(g+1)
