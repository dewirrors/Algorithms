# Задача 2 из урока 2:
# "Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)."

# Вариант решения с циклом for


import cProfile

def ev_unev_func(n):
    ev = 0
    unev = 0

    for i in str(n):
        if int(i) % 2 == 0:
            ev += 1
        else:
            unev += 1

    return ev, unev


# 5 цифр
# "les_4_task_1_1.ev_unev_func(34560)"
# 100 loops, best of 5: 2.31 usec per loop

# 10 цифр
# "les_4_task_1_1.ev_unev_func(3456013578)"
# 100 loops, best of 5: 3.79 usec per loop

# 15 цифр
# "les_4_task_1_1.ev_unev_func(345601357812345)"
# 100 loops, best of 5: 5.59 usec per loop

# 20 цифр
# "les_4_task_1_1.ev_unev_func(34560135781234536485)"
# 100 loops, best of 5: 7.39 usec per loop

# 25 цифр
# "les_4_task_1_1.ev_unev_func(3456013578123453648573900)"
# 100 loops, best of 5: 8.23 usec per loop


# 5 цифр
# cProfile.run('ev_unev_func(34560)')
# 4 function calls in 0.000 seconds

# 10 цифр
# cProfile.run('ev_unev_func(3456013578)')
# 4 function calls in 0.000 seconds

# 15 цифр
# cProfile.run('ev_unev_func(345601357812345)')
# 4 function calls in 0.000 seconds

# 20 цифр
# cProfile.run('ev_unev_func(34560135781234536485)')
# 4 function calls in 0.000 seconds

# 25 цифр
# cProfile.run('ev_unev_func(3456013578123453648573900)')
# 4 function calls in 0.000 seconds
