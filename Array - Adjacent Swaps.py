n=int(input())
l=list(map(int,input().split()))
k=n-1 if n%2!=0 else n
for i in range(0,k-1,2):
    l[i],l[i+1]=l[i+1],l[i]
print(*l)
    
