x = range(5);
for i in x:
    print(i,end = " ")

print()
print()

x = range(5,10);
for i in x:
    print(i,end = " ")

print()
print()
    
x = range(5,100,10);
for i in x:
    print(i,end = " ")
 
print()
print()
   
  
'''
0 1 2 3 4 

5 6 7 8 9 

5 15 25 35 45 55 65 75 85 95 



range() can have 3 parameters max

range(EndingPoint)
range(startingPoint, EndingPoint)
range(startingPoint, EndingPoint, incrementRule) can have 3 parameters
'''

# range() is immutable and doesn't accept any assignment of value
# TypeError: 'range' object does not support item assignment
# x = range(5);
# x[2] = 100
# for i in x:
#     print(i,end = " ")
#     
    
# if we want mutable, we use list
x = list(range(5));
x[2] = 100
for i in x:
    print(i,end = " ")
    
'''
0 1 100 3 4
'''
