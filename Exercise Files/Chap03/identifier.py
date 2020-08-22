# # looked into following functions -
# id()
# is comparator
# isinstance checker


x = [1,'two',3.0, None, '', [1,'TWO'],6]
y = [1,'two',3.0, None, '', [1,'TWO',3],6]
print(id(x))
print(id(y))
print()

'''
We get two different identifiers corresponds to the two variables x & y

1837395765696
1837395765824
'''

print(id(x[1]))
print(id(y[1]))
print()

'''
Here we get the same values as they are being accessed from same object location
3252106553072
3252106553072
'''

print(id(x[5]))
print(id(y[5]))
print(id(x[6]))
print(id(y[6]))
print()

'''
All values are accessed from same location until a different value is encountered
2674399775808
2674401700224
140728986441536
140728986441536
'''

# is command is used to check if two vars share the same location

i=0
if x[i] is y[i]:
    print('Accessed from same variable')
else:
    print('Accessed from different variable')


# to check the dataType of list/tuple - we use isinstance() function
if isinstance(x,tuple):
    print('tuple')
elif isinstance(x,list):
    print('list')
else:
    print(type(x))

x = [1,'two',3.0, None, '', [1,'TWO'],6]
y = (1,'two',3.0, None, '', [1,'TWO',3],6)
print(type(x))
print(type(y))


if x is y:
    print('same')
else:
    print('different')
'''
<class 'list'>
<class 'tuple'>
different
'''