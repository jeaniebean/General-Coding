from random import getrandbits
import math

# Miller Rabin Primality Test

def primality(n):
	#b is number of bits
	n = random.getrandbits(b)
	while (n % 2 == 0):
		n = random.getrandbits(b)

	n_1, s, d = n-1, 1, (n-1)/2
	while d % 2 == 0:
		s, d = s + 1, d / 2

	for i in range(100):
		a = random.randrange(2, n_1)
		x =  pow(a, d, n) 
		if x == 1 or x == n_1:
			continue
		else:
			for i in range(1, s):
				x = x * x % n
				if x == n_1:
					break
			else:
				return False
	print n
	return True


while not primality(512):
	primality(512)




