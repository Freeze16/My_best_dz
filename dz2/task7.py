from random import randint

comp_number = randint(0, 100)
your_number = int(input())

while comp_number != your_number:
    if comp_number > your_number:
        print('Загаданное число больше!')
    else:
        print('Загаданное число меньше!')
    your_number = int(input())

print('Вы угадали число!')
