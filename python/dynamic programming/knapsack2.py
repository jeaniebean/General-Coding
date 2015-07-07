from collections import defaultdict
from time import time

# Bounded Knapsack (Bottom-Up Memoization)

def knapsack(n, w, items):
	opt, back = defaultdict(int), defaultdict(int)

	for rw in xrange(w+1):				# rw, i, j - weight, item, copies
		for i in xrange (1, n+1):
			w_i, v_i, c_i = items[i]
			sub = [ (opt[rw-j*w_i, i-1] + j*v_i, j) for j in xrange(c_i+1) if rw >= j*w_i]
			opt[rw,i], j = max(sub)
			back[rw,i] = (rw-j*w_i, i-1), j

	def backtrace(w, n):					# backtrace
		copies, selection, w, i = defaultdict(int), '', w, n
		while w > 0 and i > 0:	
			(w, i), j = back[w,i]
			copies[i] = j
		for i in xrange(n):
			selection = selection + str(copies[i])  + ' '
		return selection

	best = opt[w, n]
	print '# non-zero cells:', len([1 for x in opt if opt[x]])
	return best, backtrace(w, n)

def main():
	(n, W), items = map(int, raw_input().split()), {}
	for i in xrange(n):
		items[i+1] = map(int, raw_input().split()) 	# weight, values, copies
	t = time()
	best, selection = knapsack(n,W,items)
	print best
	print selection
	print time() - t

if __name__ == "__main__":
	main()
