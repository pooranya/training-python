a=int(input())
s=0
c=0
while(a):
    if a&1:
        s=s+4**c
    c+=1
    a=a>>1
print(s)
