import karantools as kt
stair_lengths = {1: 1, 2: 2, 3: 4}



def count_ways(end_number):
	if end_number in stair_lengths:
		return stair_lengths[end_number]
	# for i in range(4, end_number + 1):
	stair_lengths[end_number - 3] = count_ways(end_number - 1)
	stair_lengths[end_number - 2] = count_ways(end_number - 2)
	stair_lengths[end_number - 1] = count_ways(end_number - 3)
	stair_lengths[end_number] = stair_lengths[end_number - 1] + stair_lengths[end_number - 2] + stair_lengths[end_number - 3]
	return stair_lengths[end_number]

def count_ways2(end_number):
	x = [1, 2, 4]
	if end_number <=  len(x):
		return x[end_number - 1]
	for i in range(4, end_number + 1):
		x.append(x[i - 2] + x[i - 3] + x[i - 4])
	return x[end_number - 1]

def count_ways3(end_number):
	a = 1
	b = 2
	c = 4
	count = 0
	while count < end_number // 3:
		a = a + b + c
		b = b + c + a
		c = c + a + b
		count += 1
	if end_number % 3 == 1:
		return a
	elif end_number % 3 == 2:
		return b
	else: 
		return c - a - b

print(count_ways3(12))
print(count_ways2(12))


with kt.timer():
	for i in range(10000):
		count_ways2(1000)


with kt.timer():
	for i in range(10000):
		count_ways3(1000)





