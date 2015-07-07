import random
import fractions
import time

# Finding nth Fermat's number, using Pollard Rho Prime Factorization & Miller-Rabin primality test
# for complete factorization

def _Fermat(n):
	# returns the nth Fermat number
	return 2**(2**n) + 1

def pollardRho(n, f):
	# Pollard''s Rho Algorithm

	x, d = random.randint(2, n-1), 1
	y = x
	while d == 1:
		x, y = f(x), f(f(y))			
		d = fractions.gcd(abs(x-y), n)
		if d == n:
			break
	return d 

f = lambda x: (x * x + 1) % n
'''defining a quadratic function f(x) = (x^2 + 1) mod n for Pollard''s Rho Algorithm'''

def MillerRabin(n):
	# Miller Rabin''s probabilistic primality test
	n_1, s, d = n-1, 1, (n-1)/2
	while d % 2 == 0:
		s, d = s + 1, d / 2

	'''checks for the composite number 1000 times'''
	for i in range(1000):
		a = random.randrange(2, n_1)
		x =  pow(a, d, n) 
		if not (x == 1 or x == n_1):
			for i in range(1, s):
				x = x * x % n
				if x == n_1:
					break
			else:
				return False
	print n
	return True


# Complete Factorication for Fermat(6)
t = time.time()
print "Fermat(6) = ",
n = _Fermat(6) 		
print n
print "\t =",
while not MillerRabin(n) :		
	factor = pollardRho(n, f)
	print factor, 
	n /= factor 
print "Time : \t", time.time() - t





