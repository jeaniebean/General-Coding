import sys
from collections import defaultdict

# Longest Increasing  Subsequence (Bottom-Up Memoization)

def lis(_in):						# longest common subsequence
	arr = [float('-inf')] + map(ord, _in) + [float('inf')]
	opt, back, n = defaultdict(int), defaultdict(int), len(arr)
	
	for i in xrange(n):				# bottom-up memoization
		for j in xrange(i):
			if not i or not j: opt[i], back[i] = -1, 0
			if arr[j] < arr[i] and opt[j]+1 > opt[i]:
				opt[i], back[i] = opt[j]+1, j

	def backtrace():				# backtracing
		LIS, i = '', back[n-1]
		while i:
			LIS, i = chr(arr[i]) + LIS, back[i]	
		return LIS
	
	return backtrace()

def main():
	for line in sys.stdin:
		print lis(line.strip())

if __name__ == "__main__":
        main()





