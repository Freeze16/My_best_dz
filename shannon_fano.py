from collections import Counter
from math import log2


def count(txt: str) -> list[tuple[str, int]]:  # Высчитываем абсолютную частоту
    return Counter(txt).most_common()


def pi_dict(inp: list, length: int) -> dict:  # Высчитываем относительную частоту
    j = {}
    for n, m in inp:
        pi = m / length
        j[n] = pi
    return j


def h_entropy(inp: dict) -> int:  # Считаем энтропию
    entropy = 0
    for p in inp.values():
        entropy -= p * log2(p)
    return entropy


def redundancy_evenly(h: int, n: int) -> int:  # Избыточность кода
    return int((1 - (h / n)) * 100)


def shannon_fano_encoding(keys: list[str], values: list[float], code='') -> tuple:
    i = sf_cut(values)
    pos_keys, pos_values, new_keys, new_values = keys[:i], values[:i], keys[i:], values[i:]
    '''Получаем на вход отдельно список ключей и список значений. Разделяем их (используем срез), получая
    в итоге 4 списка (2 из которых содержут просто ключи) с примерно одинаковой относительной вероятностью 
    появления символов.'''

    if len(pos_keys) == 1:
        if len(new_keys) == 1:
            return {pos_keys[0]: code + '0'}, {new_keys[0]: code + '1'}
        else:
            return {pos_keys[0]: code + '0'}, *shannon_fano_encoding(new_keys, new_values, code + '1')

    return (*shannon_fano_encoding(pos_keys, pos_values, code + '0'),
            *shannon_fano_encoding(new_keys, new_values, code + '1'))


def sf_cut(values: list[float]) -> int:
    con = [(sum(values[:i]), sum(values[i:])) for i in range(len(values))]
    a = min(con, key=lambda x: abs(x[0] - x[1]))
    '''Представляем суммы вероятностей всех срезов в виде кортежей (первый элемент - 0, второй - 1).
    Находит разницу вероятностей между 2-мя элементами каждого кортежа и берём минимальный'''

    current_summa = 0
    for i in range(len(values)):
        current_summa += values[i]
        if current_summa == a[0]:
            return i + 1


def encoding(pos: tuple[dict]) -> dict:  # Получаем из кортежа со словорями 1 единственный словарь
    j = {}
    for i in pos:
        j |= i  # Работает с python 3.9+
    return j


def translate(input_text: str, dic: dict) -> str:
    r = ''.join(dic[i] for i in input_text)
    return r


input_text = "екиббкеищбекб-пмещщщщ5шел97г8о4лш5зззззззззззззретен666"

N = 8

result_count = count(input_text)
num_uniq_char = len(result_count)
result_Pi_dict = pi_dict(result_count, len(input_text))
result_H_entropy = h_entropy(result_Pi_dict)
result_redundancy_evenly = redundancy_evenly(result_H_entropy, N)

result_shannon_fano = shannon_fano_encoding(list(result_Pi_dict.keys()), list(result_Pi_dict.values()))
result_shannon_fano_encoding = encoding(result_shannon_fano)

result_translate = translate(input_text, result_shannon_fano_encoding)
n1 = len(result_translate) / len(input_text)

result_count_new = count(result_translate)
num_uniq_char_new = len(result_count_new)
result_Pi_dict_new = pi_dict(result_count_new, len(result_translate))
result_H_entropy_new = h_entropy(result_Pi_dict_new)
result_redundancy_evenly_new = redundancy_evenly(result_H_entropy, n1)

print(result_redundancy_evenly, '%', sep='')
print(result_shannon_fano_encoding)
print(result_redundancy_evenly_new, '%', sep='')
