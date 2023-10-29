import math

a = int(input())
b = int(input()) 

if 1 <= a <= 1000 and 1 <= b <=1000:
    c = math.sqrt(a**2+b**2)
    print(c)
else:
    print('Are u stupid?')