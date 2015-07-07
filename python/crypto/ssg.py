from __future__ import division
from collections import defaultdict
import time

# Self-shrinking generator test the probability of specific sequence given specific 12 tap registers

def SSG():
	tap_list, degree = defaultdict(list), 12
	f = open('12.txt', 'r')
	for i in xrange(4):
		line = f.readline()
	for line in f.readlines():
		_line = line.strip()
		polynomial = bin(int(_line, 16))[2:]
		for j, bit in enumerate(polynomial):
			if int(bit):
				tap_list[_line].append(degree-j) 


	period, clock, expected = 2**degree - 1, 2, '0000111' #'0011100011'
	zeros, ones, len_out = 0, 0, len(expected)

	for t in tap_list:
		curr_tap, _zero, _one = tap_list[t], 0, 0
		print t, bin(int(t, 16)), curr_tap
		
		for seed in xrange(1, period):
			register, output = map(int, bin ( ((1 << degree) + seed) ) [-degree:] ), ''

			for i in xrange(degree):
				generated = False				
				
				while not generated:
					if register[0]:
						bit, generated = register[1], True
					for j in xrange(clock):
						xor_bit = 0
						for t in curr_tap:
							xor_bit = xor_bit ^ register[degree - t]
						register = register [1:] + [xor_bit]
				
				output += str(bit)

			if output[:len_out] == expected:
				if output [len_out] == '1':
					_one += 1
				else:
					_zero += 1

		zeros, ones = zeros + _zero, ones + _one	
		
	denominator = zeros + ones
	print 'Total Zero: ', zeros
	print 'Total Ones: ', ones
	print 'Probability ', (ones / denominator) * 100

start_time = time.time()
SSG()
print time.time() - start_time, 's'