# read file
f = open("day3","r+")
# since the file is just one line, so read is fine instaed of readlien()
direction = f.read()

#intial x,y co-ordinate position for santa and robot santa
s_x = 0
s_y = 0
r_x = 0
r_y = 0

# counting the turn of santa and robot santa
count = 0

# set is an unordered collection of unique elements (here house)
house = set()
# initial co-ordinate of house set
house.add((0,0))

# reading each arrow
for arrow in direction:

	if (count % 2 == 0):
		# changing x,y coordinate posiion based on arrow for santa
		if arrow == '>':
			s_x += 1
		if arrow == '<':
			s_x -= 1
		if arrow == '^':
			s_y += 1
		if arrow =='v':
			s_y -= 1

		# adding x,y co-ordinate into the set
		house.add((s_x,s_y))

	else:
		# changing x,y coordinate posiion based on arrow for robot santa
		if arrow == '>':
			r_x += 1
		if arrow == '<':
			r_x -= 1
		if arrow == '^':
			r_y += 1
		if arrow =='v':
			r_y -= 1

		# adding x,y co-ordinate into the set
		house.add((r_x,r_y))
	count += 1

# length of the set is the unique house visited
print len(house)