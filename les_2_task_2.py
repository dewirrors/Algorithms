# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

n = str(input('Введите натуральное число: '))
ev = 0
unev = 0

for i in n:
    if int(i) % 2 == 0:
        ev += 1
    else:
        unev += 1

print(f'Количество чётных цифр в числе {n}: {ev}\nКоличество нечётных цифр в числе {n}: {unev}')
