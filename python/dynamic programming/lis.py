import sys
from collections import defaultdict

# Longest Increasing  Subsequence (Top-Down Memoization)

def lis(_in):
	arr = [float('-inf')] + map(ord, _in) + [float('inf')]
	opt, back, n = defaultdict(int), defaultdict(int), len(arr)

	def search(i):                          # top-down memoization
		if i == 0: opt[i], back[i] = -1, 0
		if i not in opt:
			sub = [ (search(j)+1, j) for j in xrange(i) if arr[j] < arr[i] ]
  			opt[i], back[i] = max(sub)
		return opt[i]
	
	def backtrace():                # backtracing
		LIS, i = '', back[n-1]
		while i:
			LIS, i = chr(arr[i]) + LIS, back[i]
		return LIS

	best = search(n-1)
	return backtrace()

def main():
	for line in sys.stdin:
		print lis(line.strip())

if __name__ == "__main__":
        main()
