# CREATE

import numpy as np

class Create(object):
	def __init__(self, c, b, A):
		self.c = c
		self.b = b
		self.A = A
		self.gomory = True
		self.marks_col = None
		self.marks_row = None
		self.marks_xf = None
		self.matrix = None
		self.start()

	
	def fillMarks(self, c, b):
		size_c = int (np.size(c) + 1)
		size_b = int (np.size(b))

		temp_col = []
		temp_row = []

		for i in range(size_c + size_b):
			if i == 0:
				temp_col.append( "S0" )
			else:
				temp_col.append( "X{}".format(i) )
			pass

		for i in range(size_b):
			temp_row.append( "X{}".format(i + np.size(c) + 1) )
			pass

		temp_row.append( "F_x" )

		self.marks_col = np.array(temp_col)
		self.marks_row = np.array(temp_row)
		self.marks_xf = np.array(temp_col[ 1 : size_c ] )

		pass

	def createTable(self, c, b, A):
		_A = np.array(A.transpose() )

		temp = np.vstack( (b, _A) ) 

		temp = temp.transpose()

		edinica = np.eye(np.size(b))

		temp = np.hstack( (temp, edinica) )

		_F = np.hstack( ([0], (c * -1), np.zeros(np.size(b)) ) )

		temp = np.vstack( (temp, _F) ) 

		self.matrix = np.array(temp)

		pass
	
	def start(self):
		self.fillMarks(self.c, self.b)
		self.createTable(self.c, self.b, self.A)
		pass
