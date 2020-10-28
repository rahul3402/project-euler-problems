import karantools as kt

def find_difference(num):
	sum1 = 0
	sum2 = 0 
	for i in range(1, num + 1):
		sum1 += i ** 2
		sum2 += i
	return (sum2 ** 2) - sum1

def find_difference2(num):
	sum1 = sum(i ** 2 for i in range(1, num + 1))
	sum2 = sum(j for j in range(1, num + 1))
	return (sum2 ** 2) - sum1

def find_difference3(num):
	sum1 = sum(i ** 2 for i in range(1, num + 1))
	return (int((num / 2) * (num + 1)) ** 2) - sum1

with kt.timer():
	for i in range(100000):
		find_difference(100)
with kt.timer():
	for i in range(100000):
		find_difference2(100)
with kt.timer():
	for i in range(100000):
		find_difference3(100)