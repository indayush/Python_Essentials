#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
x ='Some String'                # Space added by itself
print('Hello, World.')


print('Hello, World. {}'.format(x))
# Valid for py version 3.6+

print(f'Hello, World. {x}')         # f is format here; space is not allowed after f keyword

print('Hello, World. %s' %x)            # Legacy Python version < 2 code format for print

