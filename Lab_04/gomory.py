# GOMORY

import numpy as np

class Gomory(object):
	def __init__(self, obj):
		self.value_xf = None
		self.index_xf = None
		self.check(obj)

	def choose(self, obj, index):
		print ("\n", obj.marks_xf[index], "=", self.value_xf[index])

		temp = np.array(obj.matrix[self.index_xf[index],:])
		temp_db = np.array( [ round(((item % 1) * -1), 2) for item in temp] )

		obj.marks_col = np.append( obj.marks_col, "X{}".format(np.size(obj.marks_col)) )
		obj.marks_row = np.insert( obj.marks_row, [-1], obj.marks_col[-1] )

		obj.matrix = np.insert( obj.matrix, [-1], temp_db, axis=0 )

		# Добавляем столбец [0, 0, 0, 1, 0]
		temp_new_x = np.zeros(np.shape(obj.matrix)[0])
		temp_new_x[-2] = 1

		temp_matrix_new_x = np.array(obj.matrix.transpose() )
		temp_matrix_new_x = np.vstack( (temp_matrix_new_x, temp_new_x) )
		obj.matrix = np.array(temp_matrix_new_x.transpose() )

		pass

	def check(self, obj):
		temp_value = np.zeros(int(np.size(obj.marks_xf)))
		# temp_index найти как заполнить -1
		# Соотвествие индексов x прии ф-ии и строк в simplex таблице
		temp_index = np.array(temp_value, int)

		for i in range(int(np.size(temp_value))):
			for j in range(int(np.size(obj.marks_row)-1)):
				if obj.marks_xf[i] == obj.marks_row[j]:
					temp_value[i] = obj.matrix[j,0]
					temp_index[i] = j
			pass

		self.value_xf = np.array(temp_value)
		self.index_xf = np.array(temp_index)

		max_value_xf = -1
		index_value_xf = -1

		for i in range(int(np.size(temp_value))):
			temp_double = self.value_xf[i] % 1
			if temp_double != 0:
				if temp_double > max_value_xf:
					max_value_xf = temp_double
					index_value_xf = i
			pass

		if index_value_xf >= 0:
			return self.choose(obj, temp_index[index_value_xf])
		else:
			obj.gomory = False
			print ("Решение является целочисленным")
			return 0

		pass
