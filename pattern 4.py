n=5
n1=n//2
for i in range(n):
    for j in range(n):
        if(i==n1 or j==n1 or j==0 and i<n1 or j==n-1 and i>n1 or i==0 and j>n1 or i==n-1 and j<n1-1):
             print("*",end="")
        else:
             print(" ",end="")
    print()
