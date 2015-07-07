import time

# Self-designed Pseudo Random Generator

def findTap(tap_hex, degree):
	tap_list = []
	tap_binary = bin(int(tap_hex, 16))[2:]
	for i, bit in enumerate(tap_binary):
		if int(bit):
			tap_list.append(degree - i) 
	return tap_list
	
def LFSR():
	num_LFSR, degree1, degree2, degree3 = 3, 15, 17, 19
	tap1, tap2, tap3 = findTap('418B', degree1), findTap('1013C', degree2), findTap('401A3', degree3)
	seed1 = seed2 = seed3 = int(time.time())
	
	register1 = map(int, bin ( ((1 << degree1) + seed1) ) [-degree1:] )
	register2 = map(int, bin ( ((1 << degree2) + seed2) ) [-degree2:] )
	register3 = map(int, bin ( ((1 << degree3) + seed3) ) [-degree3:] )
	
	maxstream, output, clock = 1000000, '', 2
	g = open('random4.txt', 'w')
	for i in xrange(maxstream):

		vote = register1[4] ^ register2[6] ^ register3[8]
		
		if vote:	bit = register1[5] ^ register2[7]
		else:		bit = register3[11]
				
		for j in xrange(clock):
			xor_bit = 0
			for pos in tap1:
				xor_bit = xor_bit ^ register1[degree1 - pos]
			register1 = register1[1:] + [xor_bit]

		for j in xrange(clock**2):
			xor_bit = 0
			for pos in tap2:
				xor_bit = xor_bit ^ register2[degree2 - pos]
			register2 = register2[1:] + [xor_bit]
	
		for j in xrange(clock**3):
			xor_bit = 0
			for pos in tap3:
				xor_bit = xor_bit ^ register3[degree3 - pos]
			register3 = register3[1:] + [xor_bit]
				
		if bit:		out = bit^register3[5]
		else:		out = register3[11]	

		print >> g, out	
			
start_time = time.time()
LFSR()
print time.time() - start_time, 's'