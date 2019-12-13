# MAIN

import numpy as np
import create
import simplex
import gomory
import output

# Вариант 18
c = np.array([7, 7, 6])
b = np.array([8, 2, 6])

A = np.array([	[2, 1, 1],
				[1, 2, 0],
				[0, 0.5, 4]	])


print ("\nИсходная simplex-таблица\n")
obj = create.Create(c, b, A)
output.show(obj)

while (obj.gomory):
	print ("\nПреобразованная simplex-таблица\n")
	simplex.Simplex(obj)
	output.show(obj)

	print ("\nВызываем метод Гомори\n")
	gomory.Gomory(obj)
	output.show(obj)
	pass

print ("\nЦелосчисленное решение")
output.result(obj)
