
def find_triplet(limit):
	for a in range(1, limit):
		for b in range(1, limit):
			if (a ** 2) + (b ** 2) == ((limit - a - b) ** 2):
				return a * b * (limit - a - b)
				
print(find_triplet(1000))