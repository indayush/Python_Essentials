#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# [] are used for a list declaration
# () are used for a tuple declaration

# Difference between tuple & list is that tuple is immutable & list is mutable

x = (1, 2, 3, 4, 5 )
for i in x:
    print('{}'.format(i),end = '; ')
'''
1; 2; 3; 4; 5; 
'''


print()
print()

x = (1, 'Ayush', 3, 4, 5 )
# x[1] = 'Adarsh'        TypeError: 'tuple' object does not support item assignment i.e. - Immutable property
for i in x:
    print('{}'.format(i),end = '; ')
'''
1; Ayush; 3; 4; 5; 
'''


print()
print()
# This is a list not an array as it can hold any data type in the list
x = [ 1, 2, 3, 4, 5 ]
for i in x:
    print('{}'.format(i),end = '; ')
'''
1; 2; 3; 4; 5; 
'''

print()
print()

x = [ 1, 'Ayush', 3, 4, 5 ]
x[1] = 'Adarsh'
for i in x:
    print('{}'.format(i),end = '; ')
'''
1; Adarsh; 3; 4; 5; 
'''

