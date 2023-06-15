def lam(a,b):
    if b == 0:
        return 0
    else:
        return a + lam(a, b-1)


x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))
print(f"The product of {x} and {y} is :", lam(x,y))

