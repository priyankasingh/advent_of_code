# read file
f = open("day3","r+")
# since the file is just one line, so read is fine instaed of readlien()
direction = f.read()

#intial x,y co-ordinate posisition
x = 0
y = 0

# set is an unordered collection of unique elements (here house)
house = set()
# initial co-ordinate of house set
house.add((0,0))

# reading each arrow
for arrow in direction:
	# changing x,y coordinate posiion based on arrow
	if arrow == '>':
		x += 1
	if arrow == '<':
		x -= 1
	if arrow == '^':
		y += 1
	if arrow =='v':
		y -= 1

	# adding x,y co-ordinate into the set
	house.add((x,y))

# length of the set is the unique house visited
print len(house)