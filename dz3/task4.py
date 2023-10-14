from collections import Counter
from task1 import enter

els = enter(input())
print('Элемент | Частота')
ans = Counter(els)
print(*[f'{i} | {ans[i]}' for i in ans], sep='\n')
