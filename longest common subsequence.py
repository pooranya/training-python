
a=input()
b=input()
k=[[0 for i in range(len(b)+1)] for i in range(len(a)+1)]
for i in k:
    print(*i)
for i in range(1,len(b)+1):
    for j in range(1,len(a)+1):
        if(b[i-1]==a[j-1]):
            k[i][j]=k[i-1][j-1]+1
        else:
            k[i][j]=max(k[i-1][j],k[i][j-1])
for i in k:
    print(*i)
print(k[-1][-1])
    
