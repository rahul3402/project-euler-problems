import karantools as kt

import math

def find_paths(limit):
	number_of_paths = [0 for i in range((limit ** 2) + 1)]
	number_of_paths[(limit ** 2) - (limit + 1)] = 2
	for last_row in range(1, limit):
		number_of_paths[(limit ** 2) - last_row] = 1
	for last_column in range(1, limit):
		number_of_paths[(limit ** 2) - (last_column * limit)] = 1
	for row in range((limit - 1), 0, -1):
		for column in range(1, limit):
			if number_of_paths[(row * limit) - column] == 0:
				number_of_paths[(row * limit) - column] = number_of_paths[(row * limit) - column + 1] + number_of_paths[((row + 1) * limit) - column]
	return number_of_paths[1]

def find_paths2(limit):
	numerator = math.factorial(2 * limit) 
	denominator = math.factorial(limit)
	return numerator // (denominator ** 2)


print(find_paths(21))

print(find_paths2(20))

with kt.timer():
	for i in range(6000):	
		find_paths(21)

with kt.timer():
	for i in range(1000000):	
		find_paths2(20)

