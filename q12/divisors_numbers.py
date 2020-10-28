
import karantools as kt
import collections

def count_divisors1(triangle_number):
	divisor = 0
	for multiple in range(1, int(triangle_number ** .5) + 1):
		if (multiple ** 2) == triangle_number:
			divisor += 1
		elif triangle_number % multiple == 0:
			divisor += 2
	return divisor

def count_divisors2(triangle_number):
	divisor = 0
	i = 1 
	while i ** 2 <= triangle_number:
		if (i ** 2) == triangle_number:
			divisor += 1
		elif triangle_number % i == 0:
			divisor += 2
		i += 1
	return divisor

def count_divisors3(triangle_number):
	primes_factors = collections.defaultdict(int)
	factor = 2
	divisors = 1
	while triangle_number % 2 == 0:
		triangle_number = triangle_number // factor
		primes_factors[2] += 1
	factor = 3
	while triangle_number > 1 and factor <= triangle_number**.5:
		while triangle_number % factor == 0:
			triangle_number = triangle_number // factor
			primes_factors[factor] += 1
		factor += 2
	if triangle_number != 1:
		primes_factors[triangle_number] += 1
	for primes in primes_factors:
		divisors *= (primes_factors[primes] + 1)
	return divisors

def count_divisors4(triangle_number):
	factor = 2
	divisors = 1
	count = 1
	while triangle_number % factor == 0:
		triangle_number = triangle_number // factor
		count += 1
	divisors *= count
	factor = 3
	while triangle_number > 1 and factor <= triangle_number**.5:
		count = 1
		while triangle_number % factor == 0:
			triangle_number = triangle_number // factor
			count += 1
		divisors *= count
		factor += 2
	if triangle_number != 1:
		divisors *= 2
	return divisors

def divisors_number1(divisors_limit):
	triangle_number = 1
	increment = 2
	while count_divisors1(triangle_number) <= divisors_limit:
		triangle_number += increment
		increment += 1
	return triangle_number 

def divisors_number2(divisors_limit):
	triangle_number = 1
	increment = 2
	while count_divisors2(triangle_number) <= divisors_limit:
		triangle_number += increment
		increment += 1
	return triangle_number

def divisors_number3(divisors_limit):
	triangle_number = 1
	increment = 2
	while count_divisors3(triangle_number) <= divisors_limit:
		triangle_number += increment
		increment += 1
	return triangle_number

def divisors_number4(divisors_limit):
	triangle_number = 1
	increment = 2
	while count_divisors4(triangle_number) <= divisors_limit:
		triangle_number += increment
		increment += 1
	return triangle_number

def divisors_number5(divisors_limit):
	number = 1
	dnumber = number + 1
	increment = 2
	while (count_divisors4(number) * count_divisors4(dnumber / 2)) <= divisors_limit:
		number += increment
		increment += 1
	return number

with kt.timer():
	for i in range(3):
		print(divisors_number3(500))

with kt.timer():
	for i in range(3):
		print(divisors_number4(500))

with kt.timer():
	for i in range(3):
		print(divisors_number5(500))


