n=input()
k=int(input())
f=len(n)-k
m=n.index(min(n[:f])
g=n[m:]
k=k-m
g=list(g)
for i in range(k):
    g.remove(max(g))
print("".join(g))




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


