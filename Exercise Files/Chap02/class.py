#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Duck:
# "self" keyword is put in every arg of the function in the class. Else we will get error
    var_sound = 'QuackKKK'
    var_walk = 'WALKING'
    

    def quack(self):
        print('Quaaack!' + self.var_sound)

    def walk(self,n):
        print('Walks like a duck. '+ self.var_walk + str(n))

def main():
    donald = Duck()
    donald.quack()
    donald.walk(7)

if __name__ == '__main__': main()

'''
Quaaack!QuackKKK
Walks like a duck. WALKING7

'''