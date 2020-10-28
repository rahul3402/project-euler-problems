import karantools as kt
def check_palindrome(number):
	number_digits = [int(x) for x in str(number)]
	for i in range(len(number_digits) // 2):
			if number_digits[i] != number_digits[len(number_digits) - 1 - i]:
				return False
	return True

def check_palindrome2(number):
	subtractant = 0
	reverse = 0
	digit = 0
	if number > 100000:
		for i in range(1,7):
			digit = ((number % (10 ** i)) - subtractant) / (10 ** (i-1)) 
			subtractant = number % (10 ** i) 
			reverse += digit * (10 ** (6-i))
	elif number>9999:
		for i in range(1,6):
			digit = ((number % (10 ** i)) - subtractant) / (10 ** (i-1))
			subtractant = number % (10 ** i) 
			reverse += digit * (10 ** (5-i))
	if reverse != number:
		return False
	return True

def check_palindrome3(number):
	curr_num = number
	reverse = 0

	while curr_num:
		digit = curr_num % 10
		curr_num //= 10
		reverse *= 10
		reverse += digit
		
	return number == reverse

def biggest_palindrome():
	biggest_palindrome = 0
	for number in range(999999, 10000, -1):
		number
		if check_palindrome3(number):
			for multiples in range(999, 100, -1):
				if number % multiples == 0 and number // multiples <1000:
					biggest_palindrome = number
					return biggest_palindrome 


def biggest_palindrome2():
	a = 999
	largest_palindrome = 0
	while a >= 100:
		if a % 11 == 0:
			b = 999
			decrement = 1
		else:
			b = 990
			decrement = 11
		while b >= a:
			if a * b <= largest_palindrome:
				break
			if check_palindrome3(a * b):
				largest_palindrome = a * b
			b -= decrement
		a -= 1
	return largest_palindrome

# print(check_palindrome3(373))
# print(biggest_palindrome2())

with kt.timer():
	for i in range(500): 
		biggest_palindrome2()

# with kt.timer():
# 	for i in range(500): 
# 		biggest_palindrome2()


		

