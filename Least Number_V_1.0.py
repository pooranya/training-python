def f(a):
    k=1
    for i in range(2,a+1):
        k*=i
    return k
n=input()
arr=f(len(n))
m=[]
for i in n:
    if i not in m:
        m.append(i)
div=1
for i in m:
    div=div*f(n.count(i))
pos=arr//div
rep=pos//len(n)
s=0
for i in n:
    s+=int(i)
s=s*rep
mul=1
val=0
for i in range(len(n)):
    val+=s*mul
    mul*=10
print(val)
if(len(m)==1):
    print("".join(n))
else:
    print(val)





#question
Given a number 'N', print the least possibe number that could be formed by removing 'K' digits.(The order of the elements should not be altered)

Input Format

N K Two space seperated integer values, where N is the given number and K is the number of elements that has to be deleted.

Constraints

1<=N<=10^25 1<=K<=10^25

Output Format

One integer value (smallest value after removing K digits form the given number N)

Sample Input 0

1234 2

Sample Output 0

12

Explanation 0

After removing rwo digits the least number is 12


