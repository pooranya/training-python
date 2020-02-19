x,y,z=map(int,input().split())
c=0
z=1+(z/100)
while(x<y):
    x=x*z
    c+=1
print(c)
