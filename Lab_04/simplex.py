# SIMPLEX

import numpy as np

class Simplex(object):
	def __init__(self, obj):
		self.S0(obj)

	def reduction(self, obj, x, y):

		mtrx = np.array(obj.matrix)
		mtrx_fill = np.zeros(np.shape(mtrx))

		# Замена обозначений переменных
		obj.marks_row[x] = obj.marks_col[y]

		delit_opor_row = mtrx[x, y]
		mnojitel_row = np.array( mtrx[:, y] / delit_opor_row )
		mnojitel_row[x] = mtrx[x, y]


		for index in np.ndindex(mtrx_fill.shape):
			if index[0] == x:
				mtrx_fill[index] = np.round ( mtrx[index] / mnojitel_row[x] , 2 )
				pass
			else:
				mtrx_fill[index] = np.round ( mtrx[index] - mtrx[x, index[1] ] * mnojitel_row[index[0]] , 2 )
				pass

		
		# return mtrx_fill
		obj.matrix = np.array(mtrx_fill)
		pass

	def F1(self, obj):

		mtrx = np.array(obj.matrix)

		opor_row = -1
		opor_col = -1

		if np.min( mtrx[-1, 1:] ) < 0:
			opor_col = np.argmin( mtrx[-1, 1:] ) + 1
		else:
			return 1
			# Конец итерации УРА!!!

		if opor_col != -1:

			temp_col = np.array ( np.where ( mtrx[:-1, opor_col] == 0, np.inf, mtrx[:-1, opor_col] ) )
			devided_S0 = np.array ( np.where ( temp_col == np.inf, np.inf, np.round (mtrx[:-1, 0] / temp_col, 2) ) )

			if np.where(devided_S0 > 0, devided_S0, np.inf).min() != np.inf:
				opor_row = np.argmin( np.where(devided_S0 > 0, devided_S0, np.inf) )
			else:
				# ERROR
				return -1
			pass

		if opor_col != -1 and opor_row != -1:
			self.reduction(obj, opor_row, opor_col)
			return self.S0(obj)

		pass

	def S0(self, obj):

		mtrx = np.array(obj.matrix)

		temp_row = -1
		opor_row = -1
		opor_col = -1

		# Получаем строку отрицательного элемента в S0
		if np.min( mtrx[:-1, 0] ) < 0:
			temp_row = np.argmin( mtrx[:-1, 0] )
		else:
			return self.F1(obj)

		if temp_row != -1:
			if np.min( mtrx[ temp_row, 1:] ) < 0:
				opor_col = np.argmin( mtrx[ temp_row, 1:] ) + 1

			else:
				# СИСТЕМА НЕ ПРАВИЛЬНОЕ ОГРАНИЧЕНИЕ РЕШЕНИЙ НЕТ!!!
				return -1

		if opor_col != -1:
			# temp_value = np.array( mtrx[:-1, 0] / mtrx[:-1, opor_col] )

			temp_col = np.array ( np.where ( mtrx[:-1, opor_col] == 0, np.inf, mtrx[:-1, opor_col] ) )
			devided_S0 = np.array ( np.where ( temp_col == np.inf, np.inf, np.round (mtrx[:-1, 0] / temp_col, 2) ) )

			if np.where(devided_S0 > 0, devided_S0, np.inf).min() != np.inf:
				opor_row = np.argmin( np.where(devided_S0 > 0, devided_S0, np.inf) )
			else:
				# ERROR
				return -1
			pass

		if opor_col != -1 and opor_row != -1:
			self.reduction(obj, opor_row, opor_col)
			return self.S0(obj)

		pass
