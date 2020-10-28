
import karantools as kt

def collatz1(start):
	largest_count = 0
	largest_number = 0 
	for i in range(start, 1, -1):
		n = i
		count = 0
		while n > 1:
			if n % 2 == 0:
				n //= 2
				count += 1
			else:
				n = (3 * n) + 1
				count += 1
		if count > largest_count:
			largest_count = count
			largest_number = i
	return largest_number

def collatz2(start):
	largest_count = 0
	largest_number = 0
	sequence_length = {} 
	for i in range(1, start, 1):
		n = i
		count = 0
		while n > 1:
			if n % 2 == 0:
				n //= 2
				if n in sequence_length:
					count += 1
					count += sequence_length[n]
					break
				else:
					count += 1
			else:
				n = (3 * n) + 1
				if n in sequence_length:
					count += 1
					count += sequence_length[n]
					break
				else:
					count += 1
		if count > largest_count:
			largest_count = count
			largest_number = i
		sequence_length[i] = count
	return largest_number

def collatz3(start):
	largest_count = 0
	largest_number = 0
	sequence_length = [0] 
	for i in range(2, start, 1):
		n = i
		count = 0
		while n > 1:
			if n % 2 == 0:
				n //= 2
				if n <= len(sequence_length):
					count += 1
					count += sequence_length[n-1]
					break
				else:
					count += 1
			else:
				n = (3 * n) + 1
				if n <= len(sequence_length):
					count += 1
					count += sequence_length[n-1]
					break
				else:
					count += 1
		if count > largest_count:
			largest_count = count
			largest_number = i
		sequence_length.append(count)
	return largest_number


def count_chain1(n):
	if n in values:
		return values[n]
	if n % 2 == 0:
		values[n] = 1 + count_chain(n // 2)
	else:
		values[n] = 2 + count_chain(((3 * n) + 1) // 2)
	return values[n]

def count_chain2(n):
	if n in values:
		return values[n]
	if n % 2 == 0:
		return 1 + count_chain2(n // 2)
	else:
		return 2 + count_chain2(((3 * n) + 1) // 2)

values = {1: 1}

def collatz4(start):
	longest = 0
	answer = 0
	for i in range(500000, 1000000):
		if count_chain2(i) > longest:
			longest = count_chain2(i)
			answer = i
	return answer



print(collatz3(999999))

with kt.timer():
	print(collatz3(999999))

with kt.timer():
	print(collatz4(999999))

