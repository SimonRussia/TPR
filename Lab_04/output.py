# OUTPUT

import numpy as np
from prettytable import PrettyTable

def show(obj):

	tab = PrettyTable()
	tab.add_column( " ", [item for item in obj.marks_row] )

	for i in range( int ( np.size(obj.marks_col) ) ):
		tab.add_column( obj.marks_col[i], [ item for item in obj.matrix[:, i] ] )

	print(tab, "\n")

	pass

def result(obj):
	temp_marks = np.array(obj.marks_xf)
	temp_marks = np.append(temp_marks, 'F_x')
	temp_value = np.zeros( np.size(temp_marks) )

	for i in range(np.size(temp_marks)):
		for j in range(np.size(obj.marks_row)):
			if temp_marks[i] == obj.marks_row[j]:
				temp_value[i] = obj.matrix[j,0]


	tab = PrettyTable()

	tab.field_names = [ item for item in temp_marks ]
	tab.add_row( [ item for item in temp_value ] )

	print(tab, "\n")

	pass
