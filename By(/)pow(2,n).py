def power(a,b):
    if(b==0):
        return 1
    else:
        m=1
        for i in range(b):
            m*=a
        return m
n,k=input().split()
k=int(k)
n=int(n[-k:])
if n%power(2,k)==0:
    print("YES")
else:
    print("NO")
