'''This is a Single line DocString'''

def test():
    '''This is a
       multiline docstring'''
    print('test')

print(test.__doc__)

help(test)
