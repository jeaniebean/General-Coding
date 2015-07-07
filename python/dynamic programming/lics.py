from collections import defaultdict
from sys import stdin

# LICS Longest Increasing Common Subsequence

def lics(a, b):
	opt, back = defaultdict(int), defaultdict(lambda:(-1,-1))
	len_a, len_b = len(a), len(b)

	# precomputation of last matched a[i] in b[i-j]
	m = defaultdict(lambda: -1)
	for i in xrange(len_a):
		for j in xrange(len_b):
			for _j in xrange(j-1, -1, -1):
				if a[i] == b[_j]: m[i, j] = _j

	def search(i, j):
		if (i, j) not in opt:
			if i < 0 or j < 0: 
				opt[i,j] = 0
			elif a[i] == b[j]:
				for _i in xrange(i):
					if a[_i] < a[i]:
						_j = m[_i, j]
						if _j >= 0 :
							first = search(_i, _j), (_i, _j)
							opt[i,j], back[i,j] = max( (opt[i, j], (i, j)), first )
				opt[i,j] += 1
			else:
				second = search(i-1, j), (i-1, j)
				third = search(i, j-1), (i, j-1)
				opt[i,j], back[i,j] = max(second, third)

		return opt[i,j]

	best = search(len_a-1, len_b-1)
	if not best:
		return 'NO LCS'

	LCS, i, j = '', len_a-1, len_b-1
	while i >= 0 and j >= 0:
		LCS = a[i] + LCS
		i, j = back[i, j]
	
	return LCS

def main():
	for line in stdin:
		_line = line
		x, y = _line.strip().split()
		print lics(x, y)

if __name__ == "__main__":
        main()


''' input :
dab dacb 
zyx xyzx
'''