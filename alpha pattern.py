n=4
for i in range(1,n+1):
    k=""
    ch='A'
    for j in range(2*i-1):
        if(j<(2*i//2)):
            k=k+ch
            ch=chr(ord(ch)+1)
            if(j==(2*i//2)-1):
                ch=chr(ord(ch)-2)
        else:
            k=k+chr(ord(ch))
            ch=chr(ord(ch)-1)
    print(k.center(2*n-1," "))
        
