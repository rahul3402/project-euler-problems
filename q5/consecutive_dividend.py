
# def smallest_multiple(num):
# 	primes_factors = collections.defaultdict(int)
# 	if num == 1:
# 		return 1
# 	for i in range(2, num + 1):
# 		print(i)
# 		for m in range(2, i+1):
# 			print(i, m)
# 			if i % m == 0 and check_prime(m):
# 				primes_factors[m] += 1
# 				i = i//m
# 				while i % m == 0 and i > 1 and primes_factors[m] < (i // m):
# 					primes_factors[m] = (i // m)
# 					i = i//m

# 	print(primes_factors)
# 	target_number = 1
# 	for prime in primes_factors:
# 		target_number *= prime ** primes_factors[prime] 
# 	return target_number
# print(smallest_multiple(6))

import collections
import karantools as kt

def check_prime(num):
	if num == 1 or num == 0:
		return False
	if num == 2:
		return True
	for i in range(3, int(num ** .5), 2):
		if num % i == 0:
			return False	
	return True

def factors(num):
	primes_factors = collections.defaultdict(int)
	factor = 2
	while num % 2 == 0:
		num = num // factor
		primes_factors[2] += 1
	factor = 3
	while num > 1 and factor <= num**.5:
		while num % factor == 0:
			num = num // factor
			primes_factors[factor] += 1
		factor += 2
	if num == 1:
		return primes_factors
	else:
		 primes_factors[num] += 1
		 return primes_factors

def smallest_multiple(limit):
	total_factors = collections.defaultdict(int)
	for i in range(limit, 1, -1):
		primes_factors = factors(i)
		for prime in primes_factors:
			if primes_factors[prime] >= total_factors[prime]:
				total_factors[prime] = primes_factors[prime]
	target_number = 1
	for numbers in total_factors:
		target_number *= (numbers ** total_factors[numbers])
	return target_number

with kt.timer():
	for i in range(100000):
		smallest_multiple(20)




