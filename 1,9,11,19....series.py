#ans 1-
le,i=1,0
l=[]
for _ in range(100):
    s=bin(i)[2:]
    s=s.zfill(le)
    s=s.replace("1","9")
    s=s.replace("0","1")
    l.append(s)
    print(s)
    i+=1
    if (i==2**le):
        le+=1
        i=0
#ans 2
n=int(input())
k=1
while(int(bin(k).replace('1','9')[2:])%n!=0):
    k+=1
print(bin(k).replace('1','9')[2:])
