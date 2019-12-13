# SIMPLEX

import numpy as np

class Simplex(object):
	def __init__(self, obj):
		self.S0(obj)

	def reduction(self, x, y, obj):
		# swap
	    _temp = obj.marks_col[y]
	    obj.marks_col[y] = obj.marks_row[x]
	    obj.marks_row[x] = _temp

	    _size = np.shape(obj.matrix)
	    _temp = np.array(obj.matrix)
	    _temp[x, y] = round( (obj.matrix[x, y] ** -1) , 3)

	    # Расчет строки
	    for i in range(_size[1]):
	        if i != y:
	            _temp[x, i] = round( (obj.matrix[x, i] / obj.matrix[x, y]) , 3)

	    # Расчет столбца
	    for j in range(_size[0]):
	        if j != x:
	            _temp[j, y] = round( (obj.matrix[j, y] / obj.matrix[x, y]) , 3) * -1

	    # Расчет остальных элементов
	    for k in range(_size[0]):
	        for l in range(_size[1]):
	            if k != x and l != y:
	                _temp[k, l] = round( (obj.matrix[k, l] - ( obj.matrix[k, y] * obj.matrix[x, l] / obj.matrix[x, y] ) ), 3 )

	    obj.matrix = _temp

	    pass

	def F1(self, obj):
	    _size = np.shape(obj.matrix)
	    flag = False
	    _min = 0
	    _y = -1

	    # Ищем опорный столбец
	    for i in range(1, _size[1]):
	        val = obj.matrix[(_size[0]-1), i]
	        if val > 0 and val > _min:
	            flag = True
	            _min = obj.matrix[(_size[0]-1), i]
	            _y = i

	    if flag == False:
	        return 0

	    _min = 1000
	    flag = False
	    _x = -1

	    # Ищем опорную строку
	    for k in range(_size[0]-1):
	        if obj.matrix[k, _y] != 0:
	            _ans = obj.matrix[k, 0] / obj.matrix[k, _y]
	            if _ans > 0 and _ans < _min:
	                flag = True
	                _min = _ans
	                _x = k

	            elif _ans > 0 and  int(_ans * 100) == int(_min * 100) and obj.matrix[k, 0] < obj.matrix[_x, 0]:
	                flag = True
	                _min = _ans
	                _x = k

	    if flag == False:
	        # Нет оптимального решения
	        print ("НЕТ ОПТИМАЛЬНОГО РЕШЕНИЯ")
	        self.brake = False
	        return -1

	    self.reduction(_x, _y, obj)

	    return self.S0(obj)

	def S0(self, obj):
	    _size = np.shape(obj.matrix)
	    flag = False
	    _min = 0
	    _x = -1

	    for i in range(_size[0]-1):
	        if obj.matrix[i, 0] < 0 and obj.matrix[i, 0] < _min:
	            flag = True
	            _min = obj.matrix[i, 0]
	            _x = i

	    if flag == False:
	        return self.F1(obj)
	        # return print ("OK")

	    flag = False
	    _min = 0
	    _y = -1

	    # Ищем опорный столбец
	    for j in range(1, _size[1]):
	        if obj.matrix[_x, j] < 0 and obj.matrix[_x, j] < _min:
	            flag = True
	            _min = obj.matrix[_x, j]
	            _y = j
	    if flag == False:
	        # Нет допуст реш
	        print ("НЕТ ДОПУСТИМЫХ РЕШЕНИЙ")
	        self.brake = False
	        return -1

	    _min = 1000
	    # Ищем опорную строку
	    for k in range(_size[0]-1):
	        if obj.matrix[k, _y] != 0:
	            _ans = obj.matrix[k, 0] / obj.matrix[k, _y]
	            if _ans > 0 and _ans < _min:
	                _min = _ans
	                _x = k

	            elif _ans > 0 and int(_ans * 100) == int(_min * 100) and obj.matrix[k, 0] < obj.matrix[_x, 0]:
	                _min = _ans
	                _x = k


	    self.reduction(_x, _y, obj)

	    return self.S0(obj)
