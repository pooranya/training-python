def f(a):
    k = 1
    for i in range(2,a+1):
        k*=i
    return k
n = input()
#no_of_arrangements
arr = f(len(n))
#removing_duplicates
m = []
for i in n:
    if i not in m:
        m.append(i)
div = 1
for i in m:
    div = div *f(n.count(i))
pos = arr//div
#repeat
rep = pos//len(n)
#sum_of_terms
s = 0
for i in n:
    s+=int(i)
s = s*rep
#number_construction
mul = 1
val = 0
for i in range(len(n)):
    val+=s*mul
    mul*=10
if(len(m)==1):
    print("".join(n))
else:
    print(val)


#question
Given a number N, find the sum of all different arrangements of N and print that as the final answer.

Input Format

A sngle integer N

Constraints

1<=N<=10^9

Output Format

One integer denoting the sum of all possible arrangements of the number N

Sample Input 0

123

Sample Output 0

1332

Explanation 0

The Possibilities are 

123
132
213
231
312
321

Whose sum will be 1332
