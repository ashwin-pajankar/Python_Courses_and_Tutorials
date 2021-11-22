class myError(Exception):
    pass

class ValueTooSmallError(myError):
    pass

class ValueTooLargeError(myError):
    pass

number = 10

try:
    i_num = int(input('Please enter an integer : '))

    if i_num < number:
        raise ValueTooSmallError
    if i_num > number:
        raise ValueTooLargeError
    else:
        print('Perfect!')
except ValueTooSmallError:
    print('The value is too small!')
except ValueTooLargeError:
    print('The value is too large!')
except Exception:
    print('Unexpected Error!')




