from decimal import *

x = .1 + .1
print(x)

x = .1 + .1 + .1 - .2
print(x)
'''
0.10000000000000003
'''

x = .1 + .1 + .1 - .3
print(x)
'''
5.551115123125783e-17 which means 17 places after 0. to this number
'''

# To handle such calculations, we import decimal and use it

a = Decimal('.1')
b = Decimal('.1')
c = Decimal('.1')
d = Decimal('.3')

x = a + b + c - d
print(x)

'''
0.0
'''