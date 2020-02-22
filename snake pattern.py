n = int(input())
val = n**2 if n%2==0 else n**2-n+1
for i in range(n):
    for j in range(n):
        if(n%2!=0 and i%2==0 or n%2==0 and i%2!=0):
            print(val,end="\t")
            val+=1
        else:
            print(val,end="\t")
            val-=1
    print()
    if(n%2!=0 and i%2==0 or n%2==0 and i%2!=0):
        val = val-n-1
    else:
        val = val-n+1
