a=20
l=[]
for i in range(2,a+1):
    while(a%i==0):
        l.append(i)
        break
print(*l)
