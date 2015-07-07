import sys
from collections import defaultdict

# Longest Common Subsequence (Bottom-Up Memoization)

def lcs(a, b):							# longest common subsequence
	opt, back = defaultdict(int), defaultdict(int)
	len_a, len_b = len(a), len(b)

	for i in xrange(1, len_a+1):			# bottom-up memoization
		for j in xrange(1, len_b+1):
			first = 1 + opt[i-1, j-1], (i-1, j-1)
			second = opt[i-1, j], (i-1, j)
			third = opt[i, j-1], (i,j-1)
			opt[i,j], back[i,j] = first if a[i-1] == b[j-1] else max(second, third)

	def backtrace(a, b):				# backtracing
		LCS, i, j = '', len_a, len_b
		a, b = '\0'+a, '\0'+b
		if not best:
			return 'NO LCS'		
		while i and j:
			if a[i] == b[j]:
				LCS = a[i] + LCS
				a, b = a[:i] + ' ' + a[i:], b[:j] + ' ' + b[j:]
			i, j = back[i,j]
		return LCS

	best = opt[len_a, len_b]
	return backtrace(a, b)

def main():
	for line in sys.stdin:
		_line = line.strip()
		a, b = map(str, _line.split())
		print lcs(a, b)

if __name__ == "__main__":
	main()