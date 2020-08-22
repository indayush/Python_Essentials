#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# simple fibonacci series
# the sum of two elements defines the next set

a, b = 0, 1
while b < 1000:
    print(b, end = ' ', flush = True)
    a, b = b, a + b

print() # line ending

'''
end = ' ' - This is for changing the default endline of the print command
print(b, flush = True) -  will also work

==================================FLUSH()=======================================
src = https://www.geeksforgeeks.org/python-sys-stdout-flush/



# Python3 program demonstrating working 
# of flush during output 

import sys 
import time 

for i in range(10): 
	print(i) 
	time.sleep(1) 

When the above program is executed, then the numbers from 0 to 9 are printed after every second on a new line, i.e., the output is automatically flushed out





# Python3 program demonstrating working 
# of flush during output 

import sys 
import time 

for i in range(10): 
	print(i, end =' ') 
	time.sleep(1) 

When the above program is executed, then there is no output for the first 9 seconds, then at the 10th, all the 10 numbers from 0 to 9 appear simultaneously in a line separated by spaces. This is because the output is buffered and it is not flushed by any means.






# Python3 program demonstrating working 
# of flush during output and usage of 
# sys.stdout.flush() function 

import sys 
import time 

for i in range(10): 
	print(i, end =' ') 
	sys.stdout.flush() 
	time.sleep(1) 

When the above program is executed, the numbers from 0 to 9 are printed every second on the same line separated by spaces. This is because calling sys.stdout.flush() forces it to “flush” the buffer, meaning that it will write everything in the buffer to the terminal, even if normally it would wait before doing so. The sys module provides functions and variables used to manipulate different parts of the Python runtime environment.


Another way of achieving the same functionality as above is setting the flush parameter of the print statement to true.
# Python3 program demonstrating working 
# of flush during output and usage of 
# flush parameter of print statement 

import sys 
import time 

for i in range(10): 
	print(i, end =' ', flush = True) 
	time.sleep(1) 

# Don't understand the working logic in print statement
'''
