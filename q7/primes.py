
# def find_prime(target_prime):
# 	not_primes = set()
# 	count = 0
# 	j = 2
# 	while count < target_prime:
# 		if j in not_primes:
# 			j += 1 
# 		elif j not in not_primes:
# 				count += 1
# 				j += 1
# 				for multiples in range(j ** 2, num + 1, j):
# 					not_primes.add(j)
# 	return j + 1
# print(find_prime(10001))

import karantools as kt

def check_prime(num):
	if num == 1 or num == 0:
		return False
	if num == 2:
		return True
	for i in range(3, int(num ** .5) + 1, 2):
		if num % i == 0:
			return False	
	return True

def check_prime2(num):
	if num == 1 or num == 0:
		return False
	for i in range(2, int(num ** .5) + 1):
		if num % i == 0:
			return False	
	return True

def find_prime(target_prime):
	count = 1
	j = 3
	while count != (target_prime):
		if check_prime(j):
			count += 1
		j += 2
	return j - 2


print(find_prime(10001))

with kt.timer():
	for i in range(50):
		find_prime(10001)

