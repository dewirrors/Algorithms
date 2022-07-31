# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

num_array = [random.randint(-100, 100) for x in range(20)]
print(f'Массив случайных чисел: {num_array}')

ind_neg_array = []
neg_array = []

for i, num in enumerate(num_array):
    if num < 0:
        ind_neg_array.append(i)
        neg_array.append(num)

max_neg = neg_array[0]

for j, neg in enumerate(neg_array):
    if neg > max_neg:
        max_neg = neg
        ind_max_neg = ind_neg_array[j]

print(f'На позиции {ind_max_neg} находится максимальный отрицательный элемент массива: {max_neg}')
