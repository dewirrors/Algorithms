# Задача 2 из урока 2:
# "Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)."

# Исходил из того, что 0 не является натуральным числом и не может быть введён пользователем.

# Вариант решения с рекурсией


import cProfile

ev = 0
unev = 0

def ev_unev_func(n):
    global ev, unev

    if n == 0:
        return ev, unev

    if n % 2 == 0:
        ev += 1
    else:
        unev += 1

    n = n // 10
    return ev_unev_func(n)


# 5 цифр
# "les_4_task_1_2.ev_unev_func(34560)"
# 100 loops, best of 5: 2.37 usec per loop

# 10 цифр
# "les_4_task_1_2.ev_unev_func(3456013578)"
# 100 loops, best of 5: 4.7 usec per loop

# 15 цифр
# "les_4_task_1_2.ev_unev_func(345601357812345)"
# 100 loops, best of 5: 8.72 usec per loop

# 20 цифр
# "les_4_task_1_2.ev_unev_func(34560135781234536485)"
# 100 loops, best of 5: 10.1 usec per loop

# 25 цифр
# "les_4_task_1_2.ev_unev_func(3456013578123453648573900)"
# 100 loops, best of 5: 13 usec per loop


# 5 цифр
# cProfile.run('ev_unev_func(34560)')
# 9 function calls (4 primitive calls) in 0.000 seconds

# 10 цифр
# cProfile.run('ev_unev_func(3456013578)')
# 14 function calls (4 primitive calls) in 0.000 seconds

# 15 цифр
# cProfile.run('ev_unev_func(345601357812345)')
# 19 function calls (4 primitive calls) in 0.000 seconds

# 20 цифр
# cProfile.run('ev_unev_func(34560135781234536485)')
# 24 function calls (4 primitive calls) in 0.000 seconds

# 25 цифр
# cProfile.run('ev_unev_func(3456013578123453648573900)')
# 29 function calls (4 primitive calls) in 0.000 seconds
