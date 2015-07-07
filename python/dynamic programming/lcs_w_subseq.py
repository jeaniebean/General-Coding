from collections import defaultdict
from sys import stdin

# LCS with subsequence

def lcs(a,b,c):
	opt, back = defaultdict(int), defaultdict(int)
	len_a, len_b, len_c = len(a), len(b), len(c)

	for i in xrange(1, len_a+1):
		for j in xrange(1, len_b+1):
			for k in xrange(1, len_c+1):
				if a[i-1] == b[j-1]: 
					first = opt[i-1, j-1, k-1] + 1, 1
					second = opt[i-1, j-1, k], 2
					opt[i,j,k], back[i,j,k] = first if a[i-1] == c[k-1] else second
				else:
					third = opt[i-1, j, k], 3
					fourth = opt[i, j-1, k], 4
					opt[i,j,k], back[i,j,k] = max(third, fourth)

	def backtrace(i, j, k):
		if not i or not j:
			return ""
		if back[i,j,k] == 1:
			return backtrace(i-1, j-1, k-1) + a[i-1]
		elif back[i,j,k] == 2:
			return backtrace(i-1, j-1, k) + a[i-1]
		elif back[i,j,k] == 3:
			return backtrace(i-1, j, k)
		else:
			return backtrace(i, j-1, k)

	result = opt[len_a, len_b, len_c]

	if not result:		
		return 'NO LCS'
		
	return backtrace(len_a, len_b, len_c)
	
def main():
	for line in stdin:
		_line = line.strip()
		x, y, z = _line.split()
		print lcs(x, y, z)

if __name__ == "__main__":
        main()


'''input :
abcbdab bdcaba bab
zzz zz a
'''