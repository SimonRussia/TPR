# MAIN

import simplex
import search
import tree
import marking
import numpy as np
from prettytable import PrettyTable


# Данные варианта 18
c = np.array( [7, 7, 6], float)
b = np.array( [8, 2, 6], float)

A = np.array( [ [2, 1, 1],
                [1, 2, 0],
                [0, 0.5, 4] ], float)


print ("ДАННЫЕ ВАРИАНТ №18")

print ("c =", c)
print ("b =", b)
print ("A =", A)


# Программа

# Шаг 0 (Создаем массивы обозначений X для графического вывода)

x_col, x_row = marking.fillMarks(c, b)
F = 0


# Шаг 1 (Получаем значения F и Х-ов)

step_1 = simplex.Simplex(c, b, A, x_col, x_row)

default_param = np.array(x_col)
default_param = np.append(default_param, x_row)
default_value = np.zeros(np.size(default_param))

for i in range(np.size(step_1.arr_row)):
	for j in range(np.size(default_param)):
		if step_1.arr_row[i] == default_param[j]:
			default_value[j] = step_1.table[i][0]

F = abs(default_value[-1])

default_table = PrettyTable()
default_table.field_names = [item for item in default_param]
default_table.add_row([item for item in default_value])

print ("\nЗначения после первого шага\n")
print(default_table, "\n")


# Шаг 2 (Полный перебор системы ограничений)

search_value, search_F = search.bruteForce(c, b, A, F)

brute_param = np.array(x_col)
brute_param = np.append(brute_param, "F")
brute_value = np.array(search_value)
brute_value = np.append(brute_value, search_F)

brute_table = PrettyTable()
brute_table.field_names = [item for item in brute_param]
brute_table.add_row([item for item in brute_value])

print ("\nРешение задачи целочисленного ЛП\n")
print(brute_table, "\n")


# Шаг 3 (Ветвление)

step_branch = tree.Branch(c, b, A, x_col, x_row)

print ("\nРекорд метод Ветвей и границ\n")

branch_table = PrettyTable()
branch_table.field_names = [item for item in step_branch.record_marks]
branch_table.add_row([item for item in step_branch.record_value])

print(branch_table, "\n")

