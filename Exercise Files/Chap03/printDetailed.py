#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.')


x = '''

This is a multi-line string


'''
print(x)

a = 5
b,c = 10,20

s = f'values are - a = {a} b = {b} c= {c}'
print(s)
'''
values are - a = 5 b = 10 c= 20
'''

# {} are positional args or placeholders
x = 'Hello, World. {}   {} {}'.format(1,2,3,4)
print(x)
# 4 is ignored as no position defined
'''
Hello, World. 1   2 3
'''

# {n} - n here specifies which value from format will go at which position
x = 'Hello, World. {1}   {2} {0}'.format(1,2,3,4)
print(x)
# 4 is ignored as no position defined
'''
Hello, World. 2   3 1
'''

# {n} - n here specifies which value from format will go at which position
# If same position is given at two places, then we will get respective value at that position
# If give 20 as position and it is invalid position which doesn't exists, then we will get - Replacement index 20 out of range for positional args tuple
x = 'Hello, World. {0}   {2} {0}'.format(1,2,3,4)
print(x)
# 4 is ignored as no position defined
'''
Hello, World. 1   3 1
'''



# {:<n} - will give error. The position is necessary
x = 'Hello, World. +"{0:<5}"+   -"{1:>5}"-   *"{2:<6}"*'.format(1,2,3,4)
print(x)
# 4 is ignored as no position defined
'''
Hello, World. +"1    "+   -"    2"-   *"3     "*
+"1    "+ = Five chars with left align
-"    2"- = Five chars with right align
*"3     "* = Six chars with left align
'''

x = 'Hello, World. +"{0:<5}"+   -"{1:>5}"-   *"{2:<06}"*'.format(1,2,321)
print(x)
# 4 is ignored as no position defined
'''
Hello, World. +"1    "+   -"    2"-   *"321000"*
+"1    "+ = Five chars with left align
-"    2"- = Five chars with right align
*"321000"* = Six chars with left align and filled with zeroes where value not present
'''

