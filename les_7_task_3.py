# Задание 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой — не больше медианы.

import random

m = 5
array = [random.randrange(0, 100) for i in range(2 * m + 1)]
print(f'Массив случайных чисел: {array}')

median_ind = 0
count_left = 0
count_right = 0

while (count_left != m) and (count_right != m):

    median = array[median_ind]
    median_ind += 1

    count_left = 0
    count_right = 0

    for i in array:
        if i < median:
            count_left += 1
        elif i > median:
            count_right += 1

print(f'Медиана массива случайных чисел: {median}')
