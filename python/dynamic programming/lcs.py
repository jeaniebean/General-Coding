import sys
from collections import defaultdict

# Longest Common Subsequence (Top-Down Memoization)

def lcs(a, b):							# longest common subsequence
	opt, back = defaultdict(int), defaultdict(int)
	len_a, len_b = len(a), len(b)

	def search(i, j):					# top-down memoization
		if not i or not j: opt[i,j] = 0
		if (i, j) not in opt:
			first = (1 + search(i-1, j-1), (i-1, j-1))
			second = search(i-1, j), (i-1, j)
			third = search(i, j-1), (i,j-1)
			opt[i,j], back[i,j] = first if a[i-1] == b[j-1] else max (second, third)
		return opt[i,j]

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
	
	best = search(len(a), len(b))
	return backtrace(a, b)

def main():
	for line in sys.stdin:
		_line = line.strip()
		a, b = map(str, line.split())
		print lcs(a, b)

if __name__ == "__main__":
	main()