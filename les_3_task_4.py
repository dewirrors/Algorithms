# Определить, какое число в массиве встречается чаще всего.

import random

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
