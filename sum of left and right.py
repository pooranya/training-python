a  = list(map(int,input().split()))
l = 0
r = len(a)-1
flag = 0
while(1):
    if(a[l]>a[r]):
        r = r - 1
        a[r]= a[r] + a[r+1]
        
    if(a[r]>a[l]):
        l = l + 1
        a[l]= a[l] + a[l-1]
    if(a[l]==a[r]):
        if(a[l]==sum(a[l+2:r-1])):
            flag = 1
            break
        else:
            l+=1
            a[l]+=a[l-1]
            continue
        
    if(r<=l):
        break
    print(r,l)
if(flag == 0):
    print("-1")
else:
    print(l+1,r-1)
