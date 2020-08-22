#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# For finding the data type of the variable
x = True
print('x is {}'.format(x))
print(type(x))


'''
7 = int
7.1 = float
None = NoneType
True = bool # true is wrong
sampleString = str
'''

x = [1,2,3]
#print('x is {}'.format(x))
print(type(x))
'''
<class 'list'>
'''

x = (1,2,3)
#print('x is {}'.format(x))
print(type(x))
'''
<class 'tuple'>
'''

x = {1,2,3}
#print('x is {}'.format(x))
print(type(x))
'''
<class 'set'>
'''


x = {'one:1','two:2','three:3','four:4','five:5'}
print(type(x))
'''
<class 'set'>
'''


x = (1,'two',3.0, None, '', [1,'TWO'])
print(type(x))
'''
<class 'tuple'>
'''

x = [1,'two',3.0, None, '', [1,'TWO']]
print(type(x))
'''
<class 'list'>
'''

# We can also get the data type of any specific element in the list
x = [1,'two',3.0, None, '', [1,'TWO']]
print(type(x[3]))
'''
<class 'NoneType'>
'''