def find_digit_sum(base, power):
	product = base ** power
	number_string = str(product)
	total = 0
	for i in number_string:
		total += int(i)
	return total

print(find_digit_sum(2,1000))


