f = open("day2","r+")
lines = f.readlines()
total_ribbon = 0

for l in lines:

	# gets the 3 sides
	s = l.rstrip().split('x') 
	# calculate bow
	bow = int(s[0]) * int(s[1]) * int(s[2])
	# new list with integer vale
	k =[int(s[0]), int(s[1]), int(s[2])]
	# remove biggest side
	k.remove(max(k))
	# calculate the two smallest side perimeter
	wrap = (k[0] * 2) + (k[1] * 2)

	total_ribbon = total_ribbon + (bow + wrap)

print total_ribbon
