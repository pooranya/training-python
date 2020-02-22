n=5
n1=n//2
for i in range(n):
    for j in range(n):
        if(j==0 or j==n-1 or i==j and i<=n1 or i+j==n-1 and i<=n1):
            print("*",end="")
        else:
             print(" ",end="")
    print()
