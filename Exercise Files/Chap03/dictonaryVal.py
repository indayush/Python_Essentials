# Key,Value pair is called a dictionary in python
# {} is used for enveloping a dictionary and is called a set
# dictionaries are mutable in nature



x = {'one:1','two:2','three:3','four:4','five:5'}
# This gives error


x = {'one':1,'two':2,'three':3,'four':4,'five':5}
x['three'] = 300
# For iterating through them -
for k,v in x.items():
    print('{} - {}'.format(k,v))
    
    
'''
one - 1
two - 2
three - 300
four - 4
five - 5

'''