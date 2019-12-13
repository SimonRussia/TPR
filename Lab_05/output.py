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
	temp_marks = np.array(obj.marks_basis)
	temp_marks = np.append(temp_marks, obj.marks_row[-1])
	temp_value = np.zeros( np.size(temp_marks) )

	for i in range(np.size(temp_marks)):
		for j in range(np.size(obj.marks_row)):
			if temp_marks[i] == obj.marks_row[j]:
				temp_value[i] = obj.matrix[j,0]


	tab = PrettyTable()

	tab.field_names = [ item for item in temp_marks ]
	tab.add_row( [ item for item in temp_value ] )

	print("Оптимальное решение")
	print(tab, "\n")

	g = round( abs( pow(obj.matrix[-1,0], -1) ), 2 )

	if obj.marks_row[-1] == 'W':
		print("Минимальный выйгрыш для [ Игрока А ] g =", g)
	else:
		print("Максимальный проигрыш для [ Игрока B ] h =", g)

	temp_value = np.array( [ round(item * g, 2) for item in temp_value] )
	temp_value[-1] = np.sum(temp_value[:-1])

	result_marks = []


	if obj.marks_row[-1] == 'W':
		for i in range(np.size(temp_value)-1):
			result_marks.append( "X{}".format(i+1) )
	else:
		for i in range(np.size(temp_value)-1):
			result_marks.append( "Y{}".format(i+1) )

	result_marks.append( 'F' )


	tab = PrettyTable()

	tab.field_names = [ item for item in result_marks ]
	tab.add_row( [ item for item in temp_value ] )

	print("\nОптимальная смешанная стратегия")
	print(tab, "\n")

	pass

def data(obj):
	size = np.shape(obj)

	name_a = []
	name_b = []

	for i in range(size[0]):
		name_a.append( "a{}".format(i+1) )

	for i in range(size[1]):
		name_b.append( "b{}".format(i+1) )


	tab = PrettyTable()
	tab.add_column( " ", [item for item in name_a] )

	for i in range( int ( np.size(name_b) ) ):
		tab.add_column( name_b[i], [ item for item in obj[:, i] ] )

	print(tab, "\n")

	pass
