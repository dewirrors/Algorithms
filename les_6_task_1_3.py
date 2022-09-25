# Задача 4 из урока 3. Определить, какое число в массиве встречается чаще всего.

import sys
import random
from collections import OrderedDict

# Создадим функцию, вычисляющую суммарную память, выделенную под переменные
def mem_count(X):
    mem_sum = 0
    for x in X:
        mem_sum += sys.getsizeof(x)
    print(f'Под переменные суммарно выделено {mem_sum} байт.')

# Напишем реализацию алгоритма решения задачи с использованием OrderedDict
random.seed(29)
num_array = [random.randint(0, 10) for x in range(20)]
print(f'Массив случайных чисел: {num_array}')

count_dict = {}

for val in num_array:
    if str(val) not in list(count_dict):
        count_dict[str(val)] = 1
    else:
        count_dict[str(val)] += 1

count_dict = OrderedDict(sorted(count_dict.items(), key=lambda x: x[1]))
max_freq = count_dict.popitem()
print(f'Число {max_freq[1]} встречается в массиве чаще всего.')
print('*' * 50)
print(sys.version)
print(sys.platform)
mem_count([num_array, count_dict, val, max_freq])

# 3.9.13 (main, Aug 25 2022, 23:51:50) [MSC v.1916 64 bit (AMD64)]
# win32
# Под переменные суммарно выделено 1172 байт.

# Вариант решения с OrderedDict требует ещё больше памяти, чем первые два решения.
# Можно заключить, что отказ от коллекций негативно сказывается на красоте и наглядности кода,
# тем не менее, позволяет оптимальнее расходовать ресурсы памяти.
