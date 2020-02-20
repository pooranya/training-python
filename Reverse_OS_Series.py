a=int(input())
k=bin(a)[2::]
odd=k[1::2]
if(len(k)%2!=0 and int(odd)==0):
    even=k[::2]
    print(int(even,2))
else:
    print("NOT PRESENT")
