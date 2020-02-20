#ans
a=int(input())
l=[]
for i in range(1,a):
    if(a%(i**2)==0):
        l.append(i**2)
print(*l)




#question
For Given a positive integer 'N', print the list of perfect square numbers that could divide the given number 'N'.

Input Format

Single positive integer 'N'

Constraints

N<10^9

Output Format

All perfect Square numbers that could divide 'N' evenly.

Sample Input 0

7236

Sample Output 0

1 4 9 36

Sample Input 1

20

Sample Output 1

1 4

