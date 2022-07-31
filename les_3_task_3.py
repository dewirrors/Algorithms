# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

int_array = [random.randint(0, 100) for x in range(20)]
print(f'Массив случайных целых чисел: {int_array}')

min_val = int_array[0]
max_val = int_array[0]

for i, val in enumerate(int_array):
    if val < min_val:
        min_val = val
        min_ind = i
    elif val > max_val:
        max_val = val
        max_ind = i

int_array[min_ind], int_array[max_ind] = int_array[max_ind], int_array[min_ind]
print(f'Изменённый массив: {int_array}')
