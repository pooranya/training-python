#answer
n=int(input())
b=sum(list(map(int,input().split())))
for i in range(n):
    if b%n==0:
        print("Live")
        break
else:
    print("Die")
 
 
 
 
#question
On 1st October 2019, Victor quitted his 13 year TV reality show director career as he lost intrest in conducting those stupid games as there were no more fun in them, and the people didnt have the adnerline pump to participate whole heartedly. The work pressure to bring out fun out of nothing and work politics and not being properly rewarded for his work, took him into strong depressionn. The entire day he didnt come out of the room. The next day he just went for a walk in the evening to try and come out of the depression, he crossed by a theatre. It was the date Joker movie was released and he thought watching a movie might help him to clear his mind. The movie actually help him to clear his mind but it did write something else in his mind. He wanted to create a game where the actual life is at stake so that the people will play with atmost sincearity and even the people will feel the fear while watching it. He named the game as "The Game of Death!". He kidnapped a person , and tied the person to the chair!

image Victor said the following words to the person: "Dead Participant, At the end of the game you may live or you may die! There might be a chance of survival or there might not be! Well sometimes its in your hands how you play! So, am gonna give you some baskets, and each basket will have some chocolates and no basket will be empty in the begenning. You will be sent out to the street with a explosive nano chip inside you, which is already injected in you. Well you can choose any random person on the street and give him/her a chocolate from one of the basket and each time you give a chocolate you have to take a chocolate from someother basket and eat it. And Continue the same till all the baskets are empty. If it is possible to make a;l the baskets empty, you will be considered a winner and you can go back home, else the nano chip will do the job. Well i have randomly chosen the number of chocolates in each box, so you might live or die. And dont try to cheat, cuz i will be watching! Your game begins now! Good luck!". Will the person Live or Die?

Input Format

Two lines of inputs, the first line of input has one integer input N, where N is the number of baskets. And the second line of input has N spaced integers denoting the number of chocolates in each basket.

Constraints

1<=N<=1000 1<=a[i]<=1000

Output Format

Print "Live" if the person can survive else print "Die"

Sample Input 0

2
1 1

Sample Output 0

Live

Explanation 0

The person can give one chocolate from one of the box to a random person and eat the chocolate from the other box, so now as the both the boxes are empty the persosn gets to live.
