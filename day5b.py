import re

f = open("day5","r+")
lines = f.readlines()
count = 0


for word in lines:

	pair = re.findall(r"([a-z]{2}).*\1", word) # or (r"(.{2}).*\1", word) like shell grep

	if pair != []:
		#print pair
		#print word
		repeat = re.findall(r"([a-z]).\1", word) # or (r"(.).\1", word) like shell grep

		if repeat != []:
			#print repeat
			count += 1

			#print word

print count

""" shell solution: cat day5 | grep "\(..\).*\1" | grep "\(.\).\1" | wc -l """