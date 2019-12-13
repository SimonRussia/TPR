# TREE

import simplex
import marking
import numpy as np
from prettytable import PrettyTable

class Branch(object):
	def __init__(self, c, b, A, x_col, x_row):
		self.c = np.array(c)
		self.b = np.array(b)
		self.A = np.array(A)
		self.arr_col = np.array(x_col)
		self.arr_row = np.array(x_row)
		self.record_marks = np.append(self.arr_col, "F")
		self.record_value = np.zeros(np.size(self.record_marks))
		self.start(self.c, self.b, self.A, self.arr_col, self.arr_row)


	# Заполняем значения X от C и F и создаем массив связей
	def fillValue(self, step):

		temp_value = np.zeros(np.size(self.record_marks))
		index_value = np.zeros(np.size(temp_value) - 1, int)

		for i in range(np.size(self.record_marks)):
			for j in range(np.size(step.arr_row)):
				if self.record_marks[i] == step.arr_row[j]:
					if self.record_marks[i] == "F":
						temp_value[i] = abs(step.table[j][0])
					else:
						temp_value[i] = step.table[j][0]
						index_value[i] = j

		return temp_value, index_value


	# Ищем нецелочисленный X
	def findFloat(self, temp_value):
		index_branch = -1

		for i in range(np.size(temp_value) - 1):
			if temp_value[i] % 1 != 0:
				index_branch = i
				break

		return index_branch


	def match(self, temp_value):
		if temp_value[-1] > self.record_value[-1]:
			self.record_value = np.array(temp_value)
		pass


	# Добавляем ограничения, для след итерации ветвления
	def addLimit(self, level, limit, index_value, _count, step, flag):

		_c = np.array(step.table[ -1, 1: ])
		_b = np.array(step.table[ 0:-1, 0 ])
		_A = np.array(step.table[ 0:-1, 1: ])
		_arr_col = np.array(step.arr_col)
		_arr_row = np.array(step.arr_row)
		_F = step.table[-1,0]

		# Добавили обознач X
		_arr_row[-1] = "X"+"{}".format(_count+1)
		_arr_row = np.append(_arr_row, "F")

		# Изменили _b
		_temp_b = (_b[index_value] - limit) * flag
		_b = np.append(_b, _temp_b)

		# Изменили _A
		_temp_lim_a = np.array(_A[index_value] * flag)
		_A = np.vstack((_A, _temp_lim_a))

		return self.start(_c, _b, _A, _arr_col, _arr_row, _F, level)

	def start(self, c, b, A, arr_col, arr_row, F=0, level=0):
	
		lvl = level + 1
		step = simplex.Simplex(c, b, A, arr_col, arr_row, F)

		# Проверка ошибки в Simplex
		if step.brake:

			_count = np.size(c) + np.size(b)

			temp_value, index_value = self.fillValue(step)

			index_branch = self.findFloat(temp_value)

			# Все X - целочисленные, сравниваем с рекордом
			if index_branch < 0:
				self.match(temp_value)

			# Если значение f(x) < рекордного, нет смысла идти дальше
			elif temp_value[-1] < self.record_value[-1]:
				pass

			# Выполняем ветвление
			else:
				left = int(temp_value[index_branch])
				print ("\n\tУровень:", lvl, "\tВЕТВЛЕНИЕ ВЛЕВО ПО", self.arr_col[index_branch], "<=", left)
				self.addLimit(lvl, left, index_value[index_branch], _count, step, -1)

				right = left + 1
				print ("\n\tУровень:", lvl, "\tВЕТВЛЕНИЕ ВПРАВО ПО", self.arr_col[index_branch], ">=", right)
				self.addLimit(lvl, right, index_value[index_branch], _count, step, 1)

		pass
