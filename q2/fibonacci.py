import karantools as kt

def fib_sum(limit):
	a = 1
	b = 2
	c = 0
	total = b
	while c < limit:
		if c % 2 == 0:
			total += c
		c = a + b
		a = b 
		b = c
		
	return total

def fib_sum2(limit):
	total = 0
	a = 1
	b = 1
	c = 2
	while c < limit:
		total += c
		a = b + c
		b = c + a
		c = a + b
	return total

print(fib_sum(4000000))
print(fib_sum2(4000000)) 

with kt.timer():
	for i in range(1000000):
		fib_sum(4000000)

with kt.timer():
	for i in range(1000000):
		fib_sum2(4000000)