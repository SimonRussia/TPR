# CREATE

import numpy as np

class Player_A(object):
	def __init__(self, A):
		self.c = None
		self.b = None
		self.A = A
		self.marks_col = None
		self.marks_row = None
		self.marks_basis = None
		self.matrix = None
		self.start()

	
	def fillMarks(self, A):
		_A = np.array(A.transpose() )

		size_c = np.shape(_A)[1]
		size_b = np.shape(_A)[0]

		self.c = np.ones(size_c) * -1
		self.b = np.ones(size_b) * -1

		temp_col = []
		temp_row = []

		for i in range(size_c + 1):
			if i == 0:
				temp_col.append( "1/g" )
			else:
				temp_col.append( "u{}".format(i) )
			pass

		for i in range(size_b):
			temp_row.append( "u{}".format(i + size_c + 1) )
			pass

		temp_row.append( "W" )

		self.marks_col = np.array(temp_col)
		self.marks_row = np.array(temp_row)
		self.marks_basis = np.array(temp_col[ 1 : (size_c + 1) ] )

		pass

	def createTable(self, c, b, A):
		_A = np.array(A * -1)

		temp = np.vstack( (b, _A) )

		temp = temp.transpose()

		_W = np.hstack( ([0], c) )

		temp = np.vstack( (temp, _W) )

		self.matrix = np.array(temp)

		pass
	
	def start(self):
		self.fillMarks(self.A)
		self.createTable(self.c, self.b, self.A)
		pass


class Player_B(object):
	def __init__(self, A):
		self.c = None
		self.b = None
		self.A = A
		self.marks_col = None
		self.marks_row = None
		self.marks_basis = None
		self.matrix = None
		self.start()

	
	def fillMarks(self, A):
		size_c = np.shape(A)[1]
		size_b = np.shape(A)[0]

		self.c = np.ones(size_c)
		self.b = np.ones(size_b)

		temp_col = []
		temp_row = []

		for i in range(size_c + 1):
			if i == 0:
				temp_col.append( "1/h" )
			else:
				temp_col.append( "v{}".format(i) )
			pass

		for i in range(size_b):
			temp_row.append( "v{}".format(i + size_c + 1) )
			pass

		temp_row.append( "Z" )

		self.marks_col = np.array(temp_col)
		self.marks_row = np.array(temp_row)
		self.marks_basis = np.array(temp_col[ 1 : (size_c + 1) ] )

		pass

	def createTable(self, c, b, A):
		_A = np.array( A.transpose() )

		temp = np.vstack( ( b, _A) )

		temp = np.array( temp.transpose() )

		_Z = np.hstack( ([0], c ) )

		temp = np.vstack( (temp, _Z) )

		self.matrix = np.array(temp)

		pass
	
	def start(self):
		self.fillMarks(self.A)
		self.createTable(self.c, self.b, self.A)
		pass
