tuple_example = ('apple', 'mango') # tuple cannot be changed or added
print(tuple_example)

# so we need to change it to list to add / change the data
list_object = list(tuple_example)
list_object.append('orange')
print(list_object)

#can make the list to tuple again
tuple_object_2 = tuple(list_object)
print(tuple_object_2)