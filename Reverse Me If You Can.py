a=input()
b=a[::-1]
if a[0]=='-':
    a='-'+str(int(a[1:][::-1]))
else:
    a=int(a[::-1])
print(a)
