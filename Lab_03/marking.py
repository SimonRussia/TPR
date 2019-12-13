# MARKING

import numpy as np

def fillMarks(c, b):
	arr_col = np.array( ["X"+"{}".format(item+1) for item in range(np.size(c))] )

	arr_row = np.array( ["X"+"{}".format(item+1+np.size(c)) for item in range(np.size(b))] )
	arr_row = np.append(arr_row, "F")

	return arr_col, arr_row