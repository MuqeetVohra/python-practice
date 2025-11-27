# defining functin
def greet():
    print('Hello World!')
# calling function
greet()

# function with parameter
def greet(Name):
    print(f'Hello {Name}!')
greet('Muqeet')

# function that returns value
def add(num1, num2):
    return num1 + num2
print(add(1,2))

# function with default parameter
def greet(Name='Guest'):
    print(f'Hello {Name}')
greet('Muqeet')
greet()

# keyword argument, to specital which parameter argument correspond to
def describe_pet(animal_type, pet_name):
    print(f'I have a {animal_type} named {pet_name}')
describe_pet(animal_type='dog',pet_name='Tommy')

# Arbitrary Argument
#using *args
def print_numbers(*args):
    for i in args:
        print(i)
print_numbers(1,2,3,4,5,6,7,8)

#using **kwargs
def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')
describe_person(Name= 'Muqeet', Age= 12)

# lambda
add = lambda x, y: x + y
print(add(4,5))

# nested function
def outer_function(x):
    def inner_function(y):
        return y * 2
    return inner_function(x)

result = outer_function(5)
print(result)

# Recursive function
num = int(input('Enter a number to find its factorial: '))
def factorial(num):
    factorial = 1
    if num == 0:
        print(f'The factorial {num} is 0')
    else:
        for i in range(1, num+1):
            factorial *= i
    return factorial
print(f'The factorial of {num} is {factorial(num)}')