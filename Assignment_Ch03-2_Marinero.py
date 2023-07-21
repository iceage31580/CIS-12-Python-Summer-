#user input
a = int(input("Please enter the first integer: "))
b = int(input("Please enter the second integer: "))
c = int(input("Please enter the third integer: "))

#Rearranges input in ascending order
if a <= b <= c:
    print(a, b, c)
elif a <= c <= b:
    print(a, c, b)
elif b <= a <= c:
    print(b, a, c)
elif b <= c <= a:
    print(b, c, a)
elif c <= a <= b:
    print(c, a, b)
else:
    print(c, b, a)