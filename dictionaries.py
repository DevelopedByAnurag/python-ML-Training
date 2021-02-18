groceries={'bananas':5,'oranges':3}
#dictionary-organize data in more  organized form . Dictionaries are unorderd
# in python 3.7  and onwards dictionaries can relied to be in order.Ordered Dicts by default
# from collections import OrderedDict (in Python <3.7 versions
print(groceries['bananas'])
#print(groceries['hello'])
print(groceries.get('bananas'))

print(groceries.get('hello'))

contacts={
    'Joe':['12345672','jkrt.ngh69@gmail.com'],
    'Jane':['98127361','Jane@gmail.com']
    
    }
contacts={
    'Joe':{'phone':'12345672','email':'jkrt.ngh69@gmail.com'},
    'Jane':{'phone':'12345672','email':'jkgh69@gmail.com'}
    
    }
print(contacts['Joe'])


sentence="I like the name Aaron because the name Aaron is the best "
word_counts={
    'I':1,
    'like':1,
    'the':3,
    'likew':1,
    'th2e':3
    }
print(word_counts.items())
print(list(word_counts.items()))
print(list(word_counts.keys()))
print(list(word_counts.values()))

print(word_counts.pop('I'))   # returns the value
print(word_counts)


word_counts.popitem()   # pop the last key-value pair
print(word_counts)

word_counts['Aaron']=2  # add the key valu pair in dictionary
print(word_counts)
print(sorted(list(word_counts.values())))

word_counts.clear()
print(word_counts)




