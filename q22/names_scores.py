import os
import karantools as kt

words = []
with open('names.txt', 'r') as f:
	line = f.read()
words = line.split(",")
words = [words[names][1:-1] for names in range(len(words))]

alphabetical_names = sorted(words)

def sum_scores(words_list):
	alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	total = 0
	for name in words_list:
		alphabetical_score = 0
		for character in name:
			for letter in alphabet:
				if letter == character:
					alphabetical_score += (alphabet.index(letter) + 1)
		total += (alphabetical_score * (words_list.index(name) + 1))
	return total

def sum_scores2(words_list):
	alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	total = 0
	for name in words_list:
		alphabetical_score = 0
		for character in name:
			alphabetical_score += (alphabet.index(character) + 1)
		total += (alphabetical_score * (words_list.index(name) + 1))
	return total

def sum_scores3(words_list):
	alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	total = 0
	index = 1
	for name in words_list:
		alphabetical_score = 0
		for character in name:
			alphabetical_score += (alphabet.index(character) + 1)
		total += (alphabetical_score * index)
		index += 1
	return total

def convert(words_list):
	alphabet = {'A': 1, 'B': 2, 'C': 3,'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}	
	alphabetical_scores = []
	for name in words_list:
		total = 0
		for letter in name:
			total += alphabet[letter]
		alphabetical_scores.append(total)
	return alphabetical_scores

def summation(scores_list):
	total = 0
	index = 1
	for score in scores_list:
		total += (index * score)
		index += 1
	return total

def convert2(words_list):
	alphabetical_scores2 = []
	for name in words_list:
		total = 0
		for letter in name:
			total += (ord(letter) - 64)
		alphabetical_scores2.append(total)
	return alphabetical_scores2

print(summation(convert2(alphabetical_names)))

# print(sum_scores2(alphabetical_names))

with kt.timer():
	for i in range(10):
		sum_scores(alphabetical_names)

with kt.timer():
	for i in range(10):
		sum_scores2(alphabetical_names)

with kt.timer():
	for i in range(10):
		sum_scores3(alphabetical_names)

with kt.timer():
	for i in range(800):
		summation(convert(alphabetical_names))

with kt.timer():
	for i in range(800):
		summation(convert2(alphabetical_names))
