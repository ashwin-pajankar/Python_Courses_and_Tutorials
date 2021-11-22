num = int(input("Please enter an integer: "))

fact = 1

if num == 0:
    print("Factorial of 0 is 1.")
else:
    for i in range (1, num+1):
        fact = fact * i
    print("The factorial of {0} is {1}.".format(num, fact))
