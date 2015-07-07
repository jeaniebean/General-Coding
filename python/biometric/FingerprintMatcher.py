import __future__, sys
from math import *

# Fingerprint matching using Hough Transform
'''constraints'''
inc = 1
#angle_thres = 5
dist_thres = 0.1

'''get input from textfile'''
def file_input(filename):
	file, prints, num = open(filename, 'r'), {}, 0
	
	for line in file:
		num += 1
		x, y, type = map(int, line.split())
		r_theta = set()
		
		for deg in xrange(0, 91, inc):
			deg_rad = radians(deg)
			r = int(x*cos(deg_rad) + y*sin(deg_rad))
			r_theta.add((r, deg))
		
		prints[x, y, type] = r_theta
	
	return num, prints

'''distance formula, r-theta parametrized version'''	
def _dist(r_phi, a_bin, b_bin):
	r, phi = r_phi
	
	theta_0 = (r for (r,t) in a_bin if t == 0)
	theta_90 = (r for (r,t) in a_bin if t == 90)
	dx1, dy1 = theta_0.next(), theta_90.next()
	theta_a = atan2(dy1, dx1)
					
	theta_0 = (r for (r,t) in b_bin if t == 0)
	theta_90 = (r for (r,t) in b_bin if t == 90)
	dx2, dy2 = theta_0.next(), theta_90.next()
	theta_b = atan2(dy2, dx2)
	
	term_1, term_2 = radians(phi-theta_a), radians(phi-theta_b)
	return abs( r * (tan(term_1) - tan(term_2)) )
	
'''pairing function'''
def pair(fp_a, fp_b):
	matched, record = {}, {}

	for pt_a in fp_a:
		a_bin = fp_a[pt_a]
		x1, y1, type_a = pt_a
		rt_pair = fp_a[pt_a] #r-theta pair of Point A
		
		for rt in rt_pair: # for every r-theta pair

			for pt_b in fp_b: #for every point in fingerprint B
				b_bin = fp_b[pt_b] 
				x2, y2, type_b = pt_b
				
				#if r-theta pair is in bin, if types match, and if points are not the same
				if rt in b_bin and type_a == type_b and (x1,y1) != (x2,y2):
					dist = _dist(rt, a_bin, b_bin)
					
					if dist < dist_thres:
						if (x1,y1) in record:
							paired, paired_dist = record[(x1,y1)]
							if dist < paired_dist:
								record[(x1,y1)] = (paired, dist)
								record[paired] = ((x1,y1), dist)
								matched[((x1,y1),paired)] = dist
						else:
							record[(x1,y1)] = ((x2,y2), dist)
							record[(x2,y2)] = ((x1,y1), dist)
							matched[((x1,y1),(x2,y2))] = dist
							
	return matched			
	
def main(argv = []):
	global inc, dist_thres
	
	if len(argv) == 3:
		inc, dist_thres = int(argv[1]), float(argv[2])

	(num_in_A, pointA), (num_in_B, pointB) = file_input("fingerprintA.txt"), file_input("fingerprintB.txt")
	tot_num = min(num_in_A, num_in_B)
	matched_pairs = pair(pointA, pointB)
	num_matched = len(matched_pairs)
	
	print 'Matched pairs:', num_matched
	print 'Percentage matched:', (num_matched / float(tot_num)) * 100
	
	for p in matched_pairs:
		print p, ':', matched_pairs[p]

if __name__ == "__main__":
	main(sys.argv)