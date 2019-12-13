# MAIN

import numpy as np
import create
import simplex
import output

# Вариант 18
A = np.array( [ [7, 9, 15, 5],
				[15, 8, 6, 4],
				[12, 0, 11, 7],
				[7, 11, 10, 12],
				[12, 2, 0, 13] ] )


print("\nДанные [ Варианта 18 ]")
output.data(A)

Player_A = create.Player_A(A)

print ("\n\nSimplex-таблица для нахождения стратегии [ Игрока А ]")
output.show(Player_A)

simplex.Simplex(Player_A)

print ("Конечная Simplex-таблица для нахождения стратегии [ Игрока А ]")
output.show(Player_A)

print ("Оптимальная стратегия [ Игрока А ]")
output.result(Player_A)


Player_B = create.Player_B(A)

print ("\n\nSimplex-таблица для нахождения стратегии [ Игрока B ]")
output.show(Player_B)

simplex.Simplex(Player_B)

print ("Конечная Simplex-таблица для нахождения стратегии [ Игрока B ]")
output.show(Player_B)

print ("Оптимальная стратегия [ Игрока B ]")
output.result(Player_B)
