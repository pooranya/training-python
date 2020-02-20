#ans 1
a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=[]
j=[]
k=[]
for i in range(len(d)):
    e.append(abs(d[i]))
f=max(e)
f1=e.index(f)
if d[f1]<0:
    g=c[f1]+(b*2)
else:
    h=c[f1]+(b*-2)
for i in range(len(c)):
    j.append(str(c[i]))
c[f1]=g
for i in range(len(c)):
    l=c[i]*d[i]
    k.append(l)
print(sum(k))
