try:
    a = 1
#    b = 0
    b = 1
    if b == 0:
        raise Exception('An exception has been raised...')
    c = a / b
except Exception as err:
    print(format(err))
else:
    print('Did not encounter any exception...')
