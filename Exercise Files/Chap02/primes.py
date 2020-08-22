#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


# Searching from 2 to n-1 and if any number divides n with 0 remainder, return result as false
def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

def listOfPrimes(n,limit):
    for n in range(limit) :
        if isprime(n):
            print(n, end=' ', flush = True)


n = 7

if isprime(n):
    print(f'{n} is prime')
else:
    print(f'{n} not prime')

listOfPrimes(n,1000)