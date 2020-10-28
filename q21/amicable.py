
import karantools as kt

def find_divisors(amicable_number):
	if amicable_number == 1:
		return 0
	divisors = 1
	factor = 2
	while factor <= amicable_number ** .5:
		if amicable_number % factor == 0:
			divisors += factor
			if factor != amicable_number ** .5:
				divisors += (amicable_number // factor)
		factor += 1
	return divisors

def find_divisors2(amicable_number):
	if amicable_number == 1:
		return 0
	divisors = 1
	if amicable_number % 2 == 0:
		step = 1
		factor = 2
	else:
		step = 2
		factor = 3
	while factor <= amicable_number ** .5:
		if amicable_number % factor == 0:
			divisors += factor
			if factor != amicable_number ** .5:
				divisors += (amicable_number // factor)
		factor += step
	return divisors

def find_divisors3(amicable_number):
	original_number = amicable_number
	total = 1
	factor = 2 
	while factor ** 2 <= amicable_number and amicable_number > 1:
		if amicable_number % factor == 0:
			largest_term = factor ** 2
			print(largest_term)
			amicable_number = amicable_number // factor
			while amicable_number % factor == 0:
				largest_term *= factor
				print(largest_term)
				amicable_number = amicable_number // factor
			print(total, largest_term, factor)
			total = total * ((largest_term - 1) // (factor - 1))
			print(total)
		if factor != 2:
			factor += 2
		else:
			factor += 1
	if amicable_number > 1:
		total *= (amicable_number + 1)
	return total - original_number


def check_amicable(limit):
	total = 0
	for i in range(2, limit):
		if i == find_divisors(find_divisors(i)) and i != find_divisors(i):
			total += i
	return total

def check_amicable2(limit):
	total = 0
	for i in range(2, limit):
		if i == find_divisors2(find_divisors2(i)) and i != find_divisors2(i):
			total += i
	return total

def check_amicable3(limit):
	total = 0
	for i in range(2, limit):
		if i == find_divisors3(find_divisors3(i)) and i != find_divisors3(i):
			total += i
	return total


print(find_divisors3(220))

# print(check_amicable(10000))
# print(check_amicable2(10000))
# print(check_amicable3(10000))

# with kt.timer():
# 	for i in range(10):
# 		check_amicable(10000)

# with kt.timer():
# 	for i in range(10):
# 		check_amicable2(10000)

# with kt.timer():
# 	for i in range(10):
# 		check_amicable3(10000)
