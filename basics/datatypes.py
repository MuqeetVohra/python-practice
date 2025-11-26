# Basics Data types (Immutable Objects)
# int
# float
# str
# bool
# complex (both real and imaginary number eg 3i)

print(type(8))
print(type(4.4))
print(type('Python'))

# changing the data type in python
num = 5
print(type(num))
print(float(num), type(float(num)))

# ingetger
a = 8
print(a)
print(f'Data type of a is {type(a)}')

# floatint point
b = 2.3
print(b)
print(f'Data type of b is {type(b)}')

# complex numbers
c = 1 + 3j
print(c)
print(f'Data type of c is {type(c)}')

# bool
d = True
print(d)
print(f'Data type of d is {type(d)}')

# string
e = 'Muqeet Vohra'
print(e)
print(f'Data type of e is {type(e)}')

# Conversion of data types

# int to float
x = 10
print(x)
print(f'Data type of x is {type(x)}')

y = float(x)
print(y)
print(f'Data type of y is {type(y)}')

# float to int
x  = 5.76
print(x)
print(f'Data type of x is {type(x)}')

y = int(x)
print(y)
print(f'Data type of y is {type(y)}')

# bool to int
a = True
b = int(a)
print(f'Data type of b is {b}')

# bool to float
b = float(a)
print(f'Data type of b is {b}')

# Strings Methods
string = 'Machine Learning  ;'
# slicing strings
print(string[2:5]) # slice from index 2 till 5-1
string=string.strip(';')
# steps in slicing
print(string[::2]) # skip 3-1 index from the string
# stripping string
print(string.strip(';'))
# string concatenation
word1 = 'Machine'
word2 = 'Learning'
word3 = word1 + word2
print(word3)
# uppercase the string
print(string.upper())

print('\n\n\nMutable Object\n\n\n')

# Mutable Objects
# List
# Set
# Dictionary
# Tuple

# list [ ]
my_list = [1,2,3,'Muqeet Vohra','V', True,3.3,5,6]
print(my_list)
print(type(my_list))
# append value at the end of the list 
my_list.append(7)
print(my_list)
# insert element at perticular index
my_list.insert(0,8) # 8 will be added at index 0
print(my_list)
# count function return the occurance of the certain value
print(my_list.count(3))
# len function count the total elements in the list
print(len(my_list))
# accessing element through indexing
print(my_list[5])
print((my_list[4])[:6]) # after accessing 4 element which is str, slicing string
# list allows redundant value
list_1 = [1,1,1,2,3,4,5,'Muqeet Vohra']
print(list_1)
# creating empty list
empty_list = []
print(empty_list)
# deleting element from the list_1
del (list_1[3])
print(list_1)
# joining two list
list_2 = [1,2,3,4,5]
list_3 = [6,7,8,9,10]
list_4 = list_2 + list_3
print(list_4)
# nested list
print('3d list or nested list')
list_5 = [1,2,3,4,[5,6,7,8,[9,10,11,12,13]]]
print(list_5[4][4][3])
list_6 = [3,5,2,1,4]
# sort function sort and modify the existing list
list_6.sort(reverse=False)
print(list_6)

# tuple ( )
tuple_1 = (1,'Muqeet Vohra',3.4,True,'V')
print(tuple_1)
print(type(tuple_1))
# converting list to tuple
my_list = [3,4,5,6]
print(my_list)
print(type(my_list))
my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))
# accessing element of tuple using indexing
print(my_tuple[3])
print((tuple_1[1])[7:]) # access string and slice it 
# finding length of tuple
print(len(tuple_1))

# set { }
my_set = {1,2,3,4,5}
print(my_set)
print(type(my_set))
# set doesn't support indexing 
# print(my_set[3]) # error
# convert a list to set
list_7 = [1,2,3,4,5]
set_1 = set(list_7)
print(set_1)
print(type(set_1))
# set doesn't allow duplicate values. It will ignore redundant values
set_2 = {1,1,2,3,4,4}
print(set_2)
# add function adds element at the end of the set
set_2.add(5)
print(set_2)
# len function count the length of the set too
print(len(set_2))
set_2.pop()
print(set_2)