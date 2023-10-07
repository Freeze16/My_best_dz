from task1 import enter

print('Элемент | Частота')
elements = enter(input())
ans = {}

for el in elements:
    ans[el] = ans.get(el, 0) + 1

print(*[f'{i} | {ans[i]}' for i in ans], sep='\n')
