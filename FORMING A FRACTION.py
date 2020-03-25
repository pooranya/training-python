#question
For given two integer 'M' and 'N' find a suitable perfect fraction x/y so that M*(X/Y) will give you the second highest factor of 'N'.

Example: M = 5,N = 64

Second highest factor of N is 32.

so, 5*(32/5) will give you 32.

Ans: 32/5

Input Format

Two space integers 'M' and 'N'

Constraints

0

Output Format

Two numbers 'X' and 'Y' seperated by '/'

Sample Input 0

5 64

Sample Output 0

32/5

Explanation 0

M = 5,N = 64

Second highest factor of N is 32.

so, 5*(32/5) will give you 32.

Ans: 32/5
  ***************************************************************************
 #answer
m=10**9
def pow(n,a):
    res=1
    while(a!=0):
        if(a&1):
            res=(res*n)%m
        a=(a>>1)
        n=(n*n)%m
    return res
t,n=map(int,input().split())
s=t*pow(2,n)
print(s)

