import hashlib

# has key text
key = 'bgvyzdsv'
# number count
num = 0

while(True):

	# doing hash of the key with number in md5
	hash = hashlib.md5(key + str(num))

	# extracting the first 5/6 digit of the hex digit
	value = hash.hexdigest()[0:6]
	# check if the value has first 5/6 digit as 0
	if value == '000000':
		break
	else:
		num += 1
	
print num