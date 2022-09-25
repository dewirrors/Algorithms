# Задача 4 из урока 3. Определить, какое число в массиве встречается чаще всего.

import sys
import random

# Создадим функцию, вычисляющую суммарную память, выделенную под переменные
def mem_count(X):
    mem_sum = 0
    for x in X:
        mem_sum += sys.getsizeof(x)
    print(f'Под переменные суммарно выделено {mem_sum} байт.')

# Напишем реализацию алгоритма решения задачи с использованием счётчика в цикле
random.seed(29)
num_array = [random.randint(0, 10) for x in range(20)]
print(f'Массив случайных чисел: {num_array}')

max_count = 0

for val in num_array:
    count = 0

    for num in num_array:
        if num == val:
            count += 1

    if count > max_count:
        max_count = count
        freq = val

print(f'Число {freq} встречается в массиве чаще всего.')
print('*' * 50)
print(sys.version)
print(sys.platform)
mem_count([num_array, max_count, val, count, num, freq])

# 3.9.13 (main, Aug 25 2022, 23:51:50) [MSC v.1916 64 bit (AMD64)]
# win32
# Под переменные суммарно выделено 388 байт.
