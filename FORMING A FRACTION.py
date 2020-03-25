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
 from math import sqrt,gcd
m,n=map(int,input().split())
s=int(sqrt(n))
x=1
for i in range(2,s+1):
    if n%i==0:
        x=n//i
        break
d=gcd(x,m)
x=x//d
m=m//d
print(x,m,sep="/")

