f = open("day2","r+")
lines = f.readlines()
total_paper = 0

for l in lines:
	# gets the 3 sides
	s = l.rstrip().split('x') 

	#get area of the box
	area = (2 * int(s[0]) * int(s[1])) + (2 * int(s[1]) * int(s[2])) + (2 * int(s[0]) * int(s[2]))
	
	#gets area of each side
	e2 = [int(s[0]) * int(s[1]), int(s[1]) * int(s[2]), int(s[0]) * int(s[2])]
	
	#calculates total wrapping paper
	total_paper = total_paper + (area + int(min(e2)))

print total_paper