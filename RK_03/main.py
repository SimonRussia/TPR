# Алгоритм ветвления

import numpy as np
from prettytable import PrettyTable


# Вариант 18
matrix = np.array([[ np.inf, 20, 18, 12, 8 ],
					[ 5, np.inf, 14, 7, 11 ],
					[ 12, 18, np.inf, 6, 11 ],
					[ 11, 17, 11, np.inf, 12 ],
					[ 5, 5, 5, 5, np.inf ]])



class Node(object):
	def __init__(self, matrix, prev):
		self.matrix = np.array(matrix)
		self.H = np.inf
		self.index_branch = None
		self.marks = None
		self.marks_branch = None
		self.prev = prev
		self.left = None
		self.right = None


class Tree(object):
	def __init__(self):
		self.head = None
		self.record = None
		self.row = np.array(["a", "b", "c", "d", "e"])
		self.col = np.array(["a", "b", "c", "d", "e"])


	def add_node(self, matrix, prev=None):
		new_node = Node(matrix, prev)

		if self.head is None:
			self.head = self.record = new_node
			self.head.marks = np.array([self.row, self.col])
			print ("\nНАЧАЛЬНАЯ МАТРИЦА\n")
			self.tableShow(self.head)
			self.reduction(self.head)
			self.root(self.head)
			print ("НИЖНЯЯ ГРАНИЦА =", self.head.H)
			self.branch(self.head)

		else:
			return new_node

	def tableShow(self, obj):

		tab = PrettyTable()
		tab.add_column(" ", [item for item in obj.marks[0, :]] )

		for i in range(np.size(obj.marks[0])):
			tab.add_column(obj.marks[1][i],	[item for item in obj.matrix[:, i]])

		print(tab, "\n")

		pass

	def show(self, obj):
		if obj.prev != None:
			self.show(obj.prev)
			print (obj.marks_branch)
		pass

	def check(self, obj):
		if obj.left != None:
			self.check(obj.left)
		else:
			if self.record.H > obj.H:
				self.record = obj

		if obj.right != None:
			self.check(obj.right)
		else:
			if self.record.H > obj.H:
				self.record = obj
		pass

	def reduction(self, obj):
		det_i = np.array(obj.matrix.min(axis=1))
		obj.matrix -= det_i[np.newaxis, :].T
		det_j = np.array(obj.matrix.min(axis=0))
		obj.matrix -= det_j
		obj.H = det_i.sum() + det_j.sum()

		pass

	def root(self, obj):
		value_max = -1
		for index, value in np.ndenumerate(obj.matrix):
			if value == 0:
				obj.matrix[index] = np.inf
				_temp_value = (obj.matrix[index[0]].min() + obj.matrix.transpose()[index[1]].min() )

				if _temp_value > value_max:
					obj.index_branch = index
					value_max = _temp_value

				obj.matrix[index] = 0

		pass

	def branch_left(self, obj):
		left_branch = np.array(obj.matrix)
		left_branch[obj.index_branch] = np.inf

		left_node = self.add_node(left_branch, obj)

		left_node.marks_branch = np.array([ "*" + obj.marks[0, obj.index_branch[0]], "*" + obj.marks[1, obj.index_branch[1]] ])
		left_node.marks = np.array( [ obj.marks[0], obj.marks[1]] )

		obj.left = left_node

		print ("\nREBRO:", left_node.marks_branch, "\tLEFT\n")
		self.tableShow(left_node)

		self.reduction(left_node)

		left_node.H += obj.H

		print ("\n\tREDUCTION_LEFT\n")
		self.tableShow(left_node)
		print ("НИЖНЯЯ ГРАНИЦА =", left_node.H)

		return left_node

	def branch_right(self, obj):
		right_branch = np.array(obj.matrix)

		# Вывести в отдельную функцию
		if (np.where(obj.marks[0] == obj.marks[1][obj.index_branch[1]], True, False)).max() and (np.where(obj.marks[1] == obj.marks[0][obj.index_branch[0]], True, False)).max():
			reverse = np.zeros(2, int)
			reverse[0] = obj.marks[0].tolist().index(obj.marks[1][obj.index_branch[1]])
			reverse[1] = obj.marks[1].tolist().index(obj.marks[0][obj.index_branch[0]])
			right_branch[reverse[0], reverse[1]] = np.inf


		right_branch = np.delete(right_branch, np.s_[obj.index_branch[0]], axis=0)
		right_branch = np.delete(right_branch, np.s_[obj.index_branch[1]], axis=1)

		right_node = self.add_node(right_branch, obj)

		right_node.marks_branch = np.array([ obj.marks[0, obj.index_branch[0]], obj.marks[1, obj.index_branch[1]] ])
		right_node.marks = np.array( [ np.delete(obj.marks[0], obj.index_branch[0]), np.delete(obj.marks[1], obj.index_branch[1])] )

		obj.right = right_node

		print ("\nREBRO:", right_node.marks_branch, "\tRIGHT\n")
		self.tableShow(right_node)

		self.reduction(right_node)

		right_node.H += obj.H

		print ("\n\tREDUCTION_RIGHT\n")
		self.tableShow(right_node)
		print ("НИЖНЯЯ ГРАНИЦА =", right_node.H)

		return right_node

	def branch_end(self, obj):
		end_branch = np.array(obj.matrix)

		ban = np.array( np.unravel_index(end_branch.argmax(), end_branch.shape) )
		ban[1] = (ban[1] + 1) % 2

		obj.index_branch = np.array(ban)

		end_branch = np.delete(end_branch, np.s_[obj.index_branch[0]], axis=0)
		end_branch = np.delete(end_branch, np.s_[obj.index_branch[1]], axis=1)

		end_node = self.add_node(end_branch, obj)

		end_node.marks_branch = np.array([ obj.marks[0, obj.index_branch[0]], obj.marks[1, obj.index_branch[1]] ])
		end_node.marks = np.array( [ np.delete(obj.marks[0], obj.index_branch[0]), np.delete(obj.marks[1], obj.index_branch[1])] )

		obj.right = end_node

		self.reduction(end_node)

		end_node.H += obj.H

		# Последний узел
		last_branch = np.array(end_node.matrix)
		last_node = self.add_node(last_branch, end_node)

		last_node.marks_branch = np.array([ end_node.marks[0,0], end_node.marks[1,0] ])

		last_node.H = end_node.H + last_node.matrix[0,0]

		return end_node, last_node

	def branch(self, obj):

		print ("\nПРИВЕДЕННАЯ МАТРИЦА\n")
		self.tableShow(obj)

		if obj.index_branch != None:

			# Ветвление вправо
			right_node = self.branch_right(obj)

			# Ветвление влево
			left_node = self.branch_left(obj)

			# Выбор более выгодного ветвления
			if left_node.H > right_node.H:
				self.record = right_node
			else:
				self.record = left_node

			# Сравнение с отсальными листами и выбор оптимального пути
			self.check(self.head)

			print ("\nВЫБРАЛИ РЕБРО:", self.record.marks_branch)

			if self.record.matrix.size > 4:
				self.root(self.record)
				self.branch(self.record)

			else:
				end_node, self.record = self.branch_end(self.record)
				print ("\nRESULT\nPath:")
				self.show(self.record)
				print ("\nMIN LENGTH PATH (H) =",self.record.H)

		pass


result = Tree()
result.add_node(matrix)
