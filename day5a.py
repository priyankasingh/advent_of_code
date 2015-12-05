import re

f = open("day5","r+")
lines = f.readlines()
count = 0


for word in lines:

	#if (word.count('a') + word.count('e') + word.count('i') + word.count('o') + word.count('u')) > 2:
	if (sum(word.count(i) for i in 'aeiou') > 2):

	# checks for repeated characters
	
		result = re.findall(r"(.)\1", word)

		if result != []:
		
			if 'ab' not in word :
				if 'cd' not in word :
					if 'pq' not in word : 
						if 'xy' not in word :
							print word
							count += 1

print count

""" shell solution cat input  | grep "[aeiou].*[aeiou].*[aeiou]" | grep "\(.\)\1" | egrep -v "(ab|cd|pq|xy)" | wc -l """