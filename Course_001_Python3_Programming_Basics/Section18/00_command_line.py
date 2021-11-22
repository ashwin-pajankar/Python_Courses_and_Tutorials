import sys

print('Program name is : ', sys.argv[0])

if len(sys.argv) > 1:
    print('Number of arguments passed = ', len(sys.argv))
    for i in range(1, len(sys.argv) ):
        print(sys.argv[i])
else:
    print('No command line arguments were entered!')
