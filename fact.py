from math import factorial as f
n=int(input())
s=""
while(n>0):
    k=1
    while f(k)<=n:
        k+=1
    n=n-f(k-1)
    s=s+str(k-1)
print(s[::-1])
        
