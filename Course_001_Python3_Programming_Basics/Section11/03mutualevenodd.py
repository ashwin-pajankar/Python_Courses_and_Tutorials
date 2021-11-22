def isEven(x):
    if x == 0:
        return True
    else:
        return isOdd(x-1)

def isOdd(x):
    if x == 0:
        return False
    else:
        return isEven(x-1)

print(isEven(3))
print(isOdd(3))

print(isEven(10))
print(isOdd(10))
