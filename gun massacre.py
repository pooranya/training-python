n,i=map(int,input().split())
k=1
while(k<=n):
    k*=2
k//=2
ans=(n-k)*2+i
print((ans%n if ans>n else ans))
