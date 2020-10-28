import karantools as kt

def sum_prime1(limit_number):
	all_numbers = [True for i in range(1, limit_number + 1)]
	count = 0 
	for i in range(1, len(all_numbers)):
		if i > 1 and all_numbers[i]:
			count += i
			for multiples in range(i ** 2, limit_number, i):
				all_numbers[multiples] = False	
	return count

def sum_prime2(limit_number):
	not_primes = set()
	count = 0
	for i in range(2, limit_number):
		if i not in not_primes:
			count += i
			for multiples in range(i ** 2, limit_number, i):
				not_primes.add(multiples)
	return count

class change_index:
	

# with kt.timer():
# 	for i in range(3):
# 		print(sum_prime1(2000000))

# with kt.timer():
# 	for i in range(3):
# 		sum_prime2(2000000)