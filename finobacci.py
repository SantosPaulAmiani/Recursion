def gen_finobacci(n):
    a = 1
    b = 1
    for x in range(n):
        yield a
        a,b = b, a+b
for number in gen_finobacci(10):
    print(number)
