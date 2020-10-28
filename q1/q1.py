import karantools as kt
import math

def add_multiples(number):
	total = 0
	for i in range(number):
		if i % 3 == 0 or i % 5 == 0:
			total += i
	return total

def add_multiples2(number):
	number -= 1
	num_five_multiples = number // 5
	num_five_pairs = num_five_multiples / 2
	num_three_multiples = number // 3
	num_three_pairs = num_three_multiples / 2 
	num_fifteen_multiples = number // 15
	num_fifteen_pairs = num_fifteen_multiples / 2
	# overlap = 0
	# for i in range(math.floor(num_five_multiples)):
	# 	if i % 3 == 0:
	# 		overlap += (5 * i)
	# print(overlap, ((15 + 15 * num_fifteen_multiples) * num_fifteen_pairs))
	total = int(((5 + num_five_multiples * 5) * num_five_pairs + (3 + num_three_multiples * 3) * num_three_pairs) - ((15 + 15 * num_fifteen_multiples) * num_fifteen_pairs))
	return total

print(add_multiples(1000))
print(add_multiples2(1000))

with kt.timer():
	add_multiples2(10000000)