import math
x,y,z=map(int,input().split())
print(math.ceil(math.log(y/x)/math.log(1+(z/100))))
