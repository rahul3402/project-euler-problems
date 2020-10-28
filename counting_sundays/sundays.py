
def count_sundays():
	count = 0
	year = 1 
	day = 2
	while year < 101:
		for month in range(1, 13):
			if month != 4 or month != 6 or month != 9 or month != 11 or month != 2:
				day += 3
				if (day % 7) == 6:
					count += 1
			elif month == 2:
				if year % 4 != 0:
					if (day % 7) == 6:
						count += 1
				else:
					day += 1
					if (day % 7) == 6:
						count += 1
			elif month == 4 or month == 6 or month == 9 or month == 11:
				day += 2
				if (day % 7) == 6:
					count += 1
		year += 1
	return count

print(count_sundays()) 


