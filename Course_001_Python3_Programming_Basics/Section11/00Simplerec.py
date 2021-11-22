def printSeries(a):
    print(a)
    if a > 0:
        printSeries(a-1)

printSeries(4)
