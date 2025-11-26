# print function
print('Practicing Python')
print('Practicing'+' '+'Python')
print(3)
print(3+3)
print('3'+'69')
print(int('3')+int('66'))

# variables
num1 = 1
num2 = '3'
sum = num1 + int(num2)
print('This sum of num1 and num2 is '+str(sum))

# declaring and initializing multiple variables in a single line
number1, number2, number3 = 3,4,5
print(number1)
print(number2)
print(number3)

# initializing multiple variables with once value
a = b = c = 10
print(a) 
print(b)
print(c)

# input function
num_1 = input('Enter the first number: ')
num_2 = input('Enter the second number: ')
# need to convert the value to int because input function take input as str
sum = int(num_1) + int(num_2)
print('The sum is ', sum)

# Q1) Swapping the values of variable
x = 2
y = 3
y, x = x, y
print(x,y)

