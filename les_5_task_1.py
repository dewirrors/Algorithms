# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и
# отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import defaultdict
import numpy as np

all_info = defaultdict(float)

n = int(input('Введите количество предприятий: '))
for c in range(n):
    comp = input('Введите наименование предприятия и прибыль за четыре квартала через пробел: ')
    numbers = comp.split(' ')
    name = numbers[0]

    profit = 0
    for i in numbers[1:]:
        profit += float(i)

    all_info[name] = profit

mean_profit = np.mean(list(all_info.values()))
less_name = []
above_name = []
for i in all_info:
    if all_info[i] < mean_profit:
        less_name.append(i)
    else:
        above_name.append(i)

print(f'Прибыль предприятий {less_name} ниже средней.')
print(f'Прибыль предприятий {above_name} выше средней.')
