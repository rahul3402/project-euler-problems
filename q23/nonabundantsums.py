
import karantools as kt

def finds_abundance(number):
	original_number = number
	total = 1
	factor = 2 
	while factor ** 2 <= number and number > 1:
		if number % factor == 0:
			largest_term = factor ** 2
			number = number // factor
			while number % factor == 0:
				largest_term *= factor
				number = number // factor
			total = total * ((largest_term - 1) // (factor - 1))
		if factor != 2:
			factor += 2
		else:
			factor += 1
	if number > 1:
		total *= (number + 1)
	if (total - original_number) > original_number:
		return True
	else:
		return False



def summation(limit):
	total = 276
	for i in range(25, limit + 1):
		valid = True
		for j in range(1, i):
			if finds_abundance(j) and finds_abundance(i - j):
				valid = False
				break
		if valid == True:
			total += i
	return total 

def summation2(limit):
	total = 276
	abundance_list = [finds_abundance(number) for number in range(0, limit)]
	for i in range(25, limit + 1):
		valid = True
		for j in range(1, i):
			if abundance_list[j] and abundance_list[i - j]:
				valid = False
				break
		if valid == True:
			total += i
	return total 


with kt.timer():
	summation2(28123)

