def square(a):
    b = a**2
    return b

def power(a, b):
    return a**b

def multiret(a, b):
    a += 1
    b += 1
    return a, b

num = square(3)
print(num)

num = power(3, 3)
print(num)

x, y = multiret(3, 5)
print("{0}, {1}".format(x, y))

