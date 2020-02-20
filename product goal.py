n,goal=map(int,input().split())
eff=list(map(int,input().split()))
day=0
product=0
while(product<goal):
    day+=1
    for i in eff:
        if day%i==0:
            product+=1
        if(product>=goal):
            break
print(day)
        
