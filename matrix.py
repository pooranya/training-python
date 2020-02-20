n=int(input())
l=[]
max=0
for i in range(n):
    l.append(list(map(int,input().split())))
k=[[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or l[i][j]==0:
            k[i][j]=l[i][j]
        else:
            k[i][j]=min(k[i-1][j],k[i-1][j-1],k[i][j-1])+1
            if k[i][j]>max:
                max=k[i][j]
for i in k:
    print(*i)
print(max)
            

