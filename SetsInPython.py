s={'blueberry','rasberry'}

s.add('strawberry')
s.add(4)
print(s)
# sets are unordered
# sets eliminate the duplicate values
# cascade lists to sets and vice versa
s.add('blueberry')



list1=[1,1,2,3,4,4,4,4,5,5,6]
print(list1)
no_duplicate_set=set(list1)
print(no_duplicate_set)
no_duplicate_list= list(no_duplicate_set)
print(no_duplicate_list)



library_1={'harry Potter','Hunger Games','Lord of the rings '}

library_2={'harry Potter','Romeo Juliet'}
#Union
all_books_in_town=library_1.union(library_2)
at_both_libraries=library_1.intersection(library_2)
diff=library_1.difference(library_2)
print(all_books_in_town)
print(at_both_libraries)
print(diff)
