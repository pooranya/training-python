#1
from math import sqrt as s
a=int(input())
if s(a)%1==0:
    print("Enemy of Odd Factor")
else:
    print("Friend of Odd Factor")

    
#2
from math import sqrt as s
a=int(input())
flag=0
if s(a)%1!=0:
    for i in range(2,a):
        if(a%i==0 and s(i)%1==0):
            flag=1
            break
else:
    flag=1
if flag==1:
    print("Enemy of Odd Factor")
else:
    print("Friend of Odd Factor")
    
#question
Given a number N, Check whether the given number is enemy of Odd factor or not. A number is said to be enemy of odd factors if the number itself shoud not have odd number of factors and none of the factors (excluding 1) should have odd number of factors, If so then print "Enemy of Odd Factor" else print "Friend of Odd Factor".

Input Format

One single integer N

Constraints

1<=N<=10^9

Output Format

Enemy of Odd Factor / Friend of Odd Factor
