# For Loop
'''laptop1 = int(input('Enter the price of the laptop: '))
laptop2 = int(input('Enter the price of the laptop: '))
laptop3 = int(input('Enter the price of the laptop: '))
laptop4 = int(input('Enter the price of the laptop: '))
laptop5 = int(input('Enter the price of the laptop: '))
'''
laptop = list()
for i in range(5): # 0, 1, 2, 3, 4
    laptop.append(int(input('Enter the price of the laptop: ')))

print(laptop[2])

numbers = [50, 100, 150, 200, 250]
for i in numbers:
    print(i)

