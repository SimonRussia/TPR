# SEARCH

import itertools
import numpy as np
from prettytable import PrettyTable

def bruteForce(c, b, A, F):
	# Получаем max значение X_i для F
	limit = ( int(F / c.min()) + 1 )

	# Получаем набор возможных натуральных значений X
	kit = np.arange(limit)

	# Создаем массив для допустимых наборов значений X-ов и записываем 0-й набор
	# Далее 0-й набор НЕ добавляем < if (np.sum(np.array(comb))) != 0: >
	arr_comb = np.zeros(np.size(c))

	for comb in itertools.product(kit, repeat=(np.size(c))):
		flag = 0
		for i in range(np.size(b)):
			if np.sum(A[i] * np.array(comb) ) <= b[i]:
				flag += 1

		if flag == np.size(b):
			result = np.sum(c * np.array(comb) )
			if result <= F:
				if (np.sum(np.array(comb))) != 0:
					arr_comb = np.vstack((arr_comb, np.array(comb)))

	return checkMaxF(arr_comb, c)

# Выбираем допустимый набор с max значением f(x)
# Ф-я возвращает набор значений X-ов при котором f(x) = max и значение ф-ии _F
def checkMaxF(arr_comb, c):
	print ("\nПеребор допустимых наборов:\n")

	arr_comb_index = 0
	_maxF = 0
	_F = 0

	for i in range(np.shape(arr_comb)[0]):
		_F = np.sum(c * arr_comb[i])
		if _F > _maxF:
			arr_comb_index = i
			_maxF = _F
		print (arr_comb[i], ", F =", _F)

	return arr_comb[arr_comb_index], _F
