#question
Given two strings s1 and s2. The task is to find a string 's2' can be obtained by rotating another string 's1'.

Input Format

The first line of input contains the string s1. The second line of the input contains the string s2

Constraints

Na enna vena kuduppen

image

Output Format

Print 1 if the estring s2 can be fobtained by rotating string s2 by two places else print 0

Sample Input 0

relearnpro
prorelearn

Sample Output 0

1

************************************************************************************************************************
#answer
s1=input()
s2=input()
for i in range(len(s2)):
    d=s2[i:]+s2[:i]
    if d==s1:
        print(1)
        break
else:
    print(0)

