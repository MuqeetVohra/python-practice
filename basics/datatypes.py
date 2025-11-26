# Basics Data types
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