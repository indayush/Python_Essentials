#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 12
y = 42

if x < y:
    # print('x < y: x is {} and y is {}'.format(y,x, y))        # No error here, just allocates value according to the first encountered var
    '''
    x < y: x is 42 and y is 12
    '''    
    print('x < y: x is {} and y is {}'.format(y,x, y))
    

# Single Line Conditional Statements
if x < y:print('x < y: x is {} and y is {}'.format(x, y))


# Else If --> elif
if x < y:
    print('x < y: x is {} and y is {}'.format(x, y))
elif x> y:
    print('x > y: x is {} and y is {}'.format(x, y))
else:
    print('The opposite condition')