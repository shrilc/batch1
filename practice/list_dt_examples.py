one = 1
two = 5
three = 10
four = 15
five = 20

list_example = [one, two, three, four, five]

print("Valid" ,type(list_example))

print(list_example[3])

# __methods__ are called dunder methods, magic methods, special methods

# List methods - 'append', 'clear', 'copy', 'count', 'extend', 'index',
# 'insert', 'pop', 'remove', 'reverse', 'sort'

list_example2 = list_example


print("Example_list1 =", list_example)
print("Example_list2 =", list_example2)


print("# Append list method")
print("# It will append | add the objects to the end of the list")
list_example.append(25)
list_example.append(30)
list_example.append(35)
list_example.append('A')
list_example.append('False')
list_example.append(True)

print(list_example)
print(list_example2)


# Deep copy
list_example2 = list_example[:]
print(list_example2)

list_example.append(25)
list_example.append(30)
list_example.append(35)
list_example.append('A')
list_example.append('False')
list_example.append(True)

print(list_example)
print(list_example2)

# clear method
##print("# Clear list method")
##list_example2.clear()
##print("List_example2:" ,list_example2)


# count method
print("# Count list method")
print("List example" , list_example)
print(list_example.count('A'))
print('B' in list_example)

# index method
print("# Index list method")
print(list_example.index('A'))

# insert method
print("# Insert list method")
list_example.insert(8, 'B')
print(list_example)

# remove method
print("# Remove list method")
list_example.remove('A') # first occurence of the object
print(list_example)

# pop method
print("# pop list method")
list_example.pop()
print(list_example)

# reverse method
print("# reverse list method")
list_example.reverse()
print(list_example)
