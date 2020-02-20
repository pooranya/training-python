a=18
l=[]
for i in range(2,a+1):
    while(a%i==0):
        a//=i
        l.append(i)
print(*l)
