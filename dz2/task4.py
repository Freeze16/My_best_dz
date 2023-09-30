a = input()
o, z = a.count('('), a.count(')')

if o > z:
    print(f'Не хватает {o - z} закрывающих скобок!')
elif z > o:
    print(f'Не хватает {z - o} открывающих скобок!')
else:
    print('Всё в порядке!')
