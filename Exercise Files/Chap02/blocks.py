#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 42
y = 73

if x < y:
    print('x < y: x is {} and y is {}'.format(x, y))
    print(f'x < y: x is {x} and y is {y}')
    z = 12

print(z)
# This means the scope of z is independent of where it is declared
