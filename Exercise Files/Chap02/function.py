#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# def function(n):
def function(n = 1):        # Setting n as 1 so that when fun called with no args, it will take value as 1 by default
    print(n)

function(47)
function()
x = function(45)

print(x)        # None is received because of no return statement

