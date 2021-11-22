lower = 2
upper = 10000

for num in range (lower, upper+1):
    for i in range(2, num):
        if(num % i) == 0:
            break
    else:
        print(num)
