a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
    print(a)
elif a < b > c:
    print(b)
else:
    print(c)
    

#or another possible solution if we can't use loop in our case:

#max_value = max(a, b, c)

#print(max_value)