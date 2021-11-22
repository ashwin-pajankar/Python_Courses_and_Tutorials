def printHello( first_name ):
    print("Hello {0}".format(first_name))

def printHello1( first_name, last_name ):
    print("Hello {0}, {1}".format(first_name, last_name))

def printHello2( first_name, msg='Good Morning!'):
    print("Hello {0}, {1}".format(first_name, msg))



#printHello('Ashwin')
#printHello('Thor')

#printHello1('Ashwin', 'Pajankar')
#printHello1(first_name='Ashwin', last_name='Pajankar')
printHello1(last_name='Pajankar', first_name='Ashwin')
printHello1('Thor', 'Odinson')

#printHello2('Ashwin', 'Good Evening!')
#printHello2('Thor')
