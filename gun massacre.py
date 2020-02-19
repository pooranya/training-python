n,i=map(int,input().split())
k=1
while(k<=n):
    k*=2
k//=2
print(((n-k)*2+i)%n)
