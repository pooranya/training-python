n1=list(input())
n2=list(input())
n3=n1.copy()
n4=n2.copy
for i in range(len(n1)):
    if i in range(len(n2)):
        n1.remove(i)
        n2.remove(i)
k=len(n3)+len(n4)
l=['F','L','A','M','E','S']
while(len(l)>1):
    if k%len(l)==0:
        l=l[:-1]
    else:
        m=k%len(l)
        left=l[:m-1]
        right=l[m:]
        l=right+left
print(l[0])
