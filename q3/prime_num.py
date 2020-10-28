import karantools as kt
from tqdm import tqdm



# def check_prime2(num):
# 	is_not_prime = set()
# 	biggest_prime = 0
# 	for i in tqdm(range(2, num)):
# 		if i not in is_not_prime:
# 			for mutiples in tqdm(range(2, num // i)):
# 				is_not_prime.add(i * mutiples)
# 			if num % i == 0:
# 				biggest_prime = i
# 	return biggest_prime
# check_prime(i) == True

# 	print(primes_array)
# def biggest_prime_factor(num):
# 	prime_factor = 0
# 	largest_factor = 0
# 	if num == 1:
# 		return 1
# 	for i in range(2, num ** .5):
# 		if num % i == 0:
# 			largest_factor = num/i
# 			for number in range(2, largest_factor)
# 				if num % number = 0 and check_prime(number) 
# 					largest_ prime_factor = i
# 	return prime_factor

def check_prime(num):
	if num == 1 or num == 0:
		return False
	for i in range(2, int(num ** .5)):
		if num % i == 0:
			return False	
	return True

def biggest_prime_factor(num):
	prime_factor = 0
	if num == 1:
		return 1
	for i in range(2, int(num ** .5 + 1)):
		if num % i == 0 and check_prime(num/i):
			prime_factor = int(num/i)
		elif num % i == 0 and check_prime(i) and i > prime_factor:
			prime_factor = i
	return prime_factor

def biggest_prime_factor2(num):
	factor = 2
	largest_factor = 0
	while num>1:
		if num % factor == 0:
			largest_factor = factor
			num = num / factor
			while num % factor == 0:
				num = num / factor
		factor += 1
	return largest_factor

def biggest_prime_factor3(num):
	factor = 2
	largest_factor = 0
	while num % 2 == 0:
		largest_factor = factor
		num = num/factor
	factor = 3
	while num>1:
		if num % factor == 0:
			largest_factor = factor
			num = num/factor
			while num % factor == 0:
				num = num/factor
		factor += 2
	return largest_factor

def biggest_prime_factor4(num):
	factor = 2
	largest_factor = 0
	while num % 2 == 0:
		largest_factor = factor
		num = num/factor
	factor = 3
	while num>1 and factor <= num**.5:
		if num % factor == 0:
			largest_factor = factor
			num = num/factor
			while num % factor == 0:
				num = num/factor
		factor += 2
	if num == 1:
		return largest_factor
	else:
		return int(num)

print(biggest_prime_factor4(600851475143))

with kt.timer():
	biggest_prime_factor4(600851475143)



