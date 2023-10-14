from collections import Counter
from task1 import enter

print('Элемент | Частота')
els = enter(input())
ans = Counter(els)
print(*[f'{i} | {ans[i]}' for i in ans], sep='\n')
