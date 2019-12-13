# TPR Lab01 && Lab02

import numpy as np
from prettytable import PrettyTable


class Simplex(object):
	def __init__(self, c, b, A, col, row):
		self.c = c
		self.b = b
		self.A = A
		self.arr_col = col
		self.arr_row = row

	def graph(self, x=-1, y=-1):

		if x != -1 and y != -1:
			_y = y - 1

			print ("Замена опорной строки на опорный столбец:", self.arr_row[x], "<=>", self.arr_col[_y])

			# swap
			_temp = self.arr_col[_y]
			self.arr_col[_y] = self.arr_row[x]
			self.arr_row[x] = _temp

		tab = PrettyTable()
		tab.add_column(" ",					[self.arr_row[0], self.arr_row[1], self.arr_row[2], "F"])
		tab.add_column("S0", 				[item for item in self.table[:, 0]])
		tab.add_column(self.arr_col[0], 	[item for item in self.table[:, 1]])
		tab.add_column(self.arr_col[1],		[item for item in self.table[:, 2]])
		tab.add_column(self.arr_col[2],		[item for item in self.table[:, 3]])

		print(tab, "\n")

		pass

	def calculate(self, x, y):

	    # print ('Опорная строка:', x, 'Опорный столбец:', y)

	    _size = np.shape(self.table)
	    _temp = np.array(self.table)
	    _temp[x, y] = round( (self.table[x, y] ** -1) , 2)

	    # print (_temp, '\n')

	    # Расчет строки
	    for i in range(_size[1]):
	        if i != y:
	            _temp[x, i] = round( (self.table[x, i] / self.table[x, y]) , 2)

	    # print (_temp, '\n')
	    # Расчет столбца
	    for j in range(_size[0]):
	        if j != x:
	            _temp[j, y] = round( (self.table[j, y] / self.table[x, y]) , 2) * -1

	    # print (_temp, '\n')
	    # Расчет остальных элементов
	    for k in range(_size[0]):
	        for l in range(_size[1]):
	            if k != x and l != y:
	                _temp[k, l] = round( (self.table[k, l] - ( self.table[k, y] * self.table[x, l] / self.table[x, y] ) ), 2 )

	    self.table = _temp

	    # Вывод в округленном виде.
	    np.set_printoptions(precision=2, suppress=True)
	    # print (_temp, '\n')
	    self.graph(x, y)

	    # return _temp
	    pass

	def scanF(self):
	    _size = np.shape(self.table)
	    flag = False
	    _min = 0
	    _y = -1

	    # Ищем опорный столбец
	    for i in range(1, _size[1]):
	        val = self.table[(_size[0]-1), i]
	        if val > 0 and val > _min:
	            flag = True
	            _min = self.table[(_size[0]-1), i]
	            _y = i

	    if flag == False:
	        # Решение является оптимальным
	        print ("Решение является оптимальным")
	        return self.graph()

	    _min = 1000
	    flag = False
	    _x = -1

	    # Ищем опорную строку
	    for k in range(_size[0]-1):
	        if self.table[k, _y] != 0:
	            _ans = self.table[k, 0] / self.table[k, _y]
	            if _ans > 0 and _ans < _min:
	                flag = True
	                _min = _ans
	                _x = k

	    if flag == False:
	        # Нет оптимального решения
	        return print ("НЕТ ОПТИМАЛЬНОГО РЕШЕНИЯ")

	    # self.table = np.array(self.calculate(_x, _y))
	    self.calculate(_x, _y)

	    return self.scanS0()

	def scanS0(self):
	    _size = np.shape(self.table)
	    flag = False
	    _min = 0
	    _x = -1

	    for i in range(_size[0]-1):
	        if self.table[i, 0] < 0 and self.table[i, 0] < _min:
	            flag = True
	            _min = self.table[i, 0]
	            _x = i

	    if flag == False:
	        return self.scanF()
	        # return print ("OK")

	    flag = False
	    _min = 0
	    _y = -1

	    # Ищем опорный столбец
	    for j in range(1, _size[1]):
	        if self.table[_x, j] < 0 and self.table[_x, j] < _min:
	            flag = True
	            _min = self.table[_x, j]
	            _y = j
	    if flag == False:
	        # Нет допуст реш
	        print ("НЕТ ДОПУСТИМЫХ РЕШЕНИЙ")
	        return -2

	    _min = 1000
	    # Ищем опорную строку
	    for k in range(_size[0]-1):
	        if self.table[k, _y] > 0:
	            _ans = self.table[k, 0] / self.table[k, _y]
	            if _ans > 0 and _ans < _min:
	                _min = _ans
	                _x = k

	    # self.table = np.array(self.calculate(_x, _y))
	    self.calculate(_x, _y)

	    return self.scanS0()
	
	def start(self):
		size_A = np.shape(self.A)

		# self.arr_col = np.array(["X1", "X2", "X3"])
		# self.arr_row = np.array(["X4", "X5", "X6"])

		self.table = np.zeros( ( (size_A[0]+1), (size_A[1]+1) ) )

		for i in range(size_A[0]):
			self.table[i, 0] = self.b[i]

		for j in range(size_A[1]):
			self.table[size_A[0], j+1] = self.c[j]

		for k in range(size_A[0]):
			for l in range(size_A[1]):
				self.table[k,l+1] = self.A[k,l]

		print ("\nИсходная simplex-таблица")
		self.graph()

		self.scanS0()

		pass


# Data of Variant

c = np.array( [7, 7, 6], float)

b = np.array( [8, 2, 6], float)

A = np.array( [ [2, 1, 1],
                [1, 2, 0],
                [0, 0.5, 4] ], float)


_c = np.array(b) * -1

_b = np.array(c) * -1

_A = np.array(A.transpose()) * -1


# Calling Simplex

# ПРЯМАЯ ЗАДАЧА
print ("\n", "#"*20, "ПРЯМАЯ ЗЛП", "#"*20)

arr_col = np.array(["X1", "X2", "X3"])
arr_row = np.array(["X4", "X5", "X6"])

straight = Simplex(c, b, A, arr_col, arr_row)
straight.start()

# ДВОЙСТВЕННАЯ ЗАДАЧА
print ("\n", "#"*20, "ДВОЙСТВЕННАЯ ЗЛП", "#"*20)

arr_col = np.array(["Y1", "Y2", "Y3"])
arr_row = np.array(["Y4", "Y5", "Y6"])

dual = Simplex(_c, _b, _A, arr_col, arr_row)
dual.start()
