# Simple if else statement
a = 30
b = 50

if a > b:
    print('a is the greater number')
else:
    print('b is the greater number')

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

if a > b:
    print('First number is the greater number')
else:
    print('Second is the greater number')

# if elif else 
a = 15
b = 25
c = 35

if b<a>c:
    print('a is the greatest')
elif a<b>c:
    print('b is the greatest')
else:
    print('c is the greatest')

# nested if statement
a = 20
b = 140
c = 60

if a > b:
    if a > c:
        print('a is the greatest')
    else:
        print('c is the greatest')
else:
    if b > c:
        print('b is the greatest')
    else:
        print('c is the greatest')
