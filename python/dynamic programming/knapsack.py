from collections import defaultdict
from time import time

# Bounded Knapsack (Top-Down Memoization)

def knapsack(n, w, items):
	opt, back = defaultdict(int), defaultdict(int)

	def search(w, i):						# top-down memoization
		if not w or not i: 
			opt[w,i], back[w,i] = 0, 0
		if (w, i) not in opt:
			w_i, v_i, c_i = items[i]
			sub = [(search(w-j*w_i, i-1) + j*v_i, j) for j in xrange(c_i+1) if w >= j*w_i]
			opt[w,i], j = max(sub)
			back[w,i] = (w-j*w_i, i-1), j
		return opt[w,i]
	
	def backtrace(w, n):					# backtrace
		copies, selection, w, i = defaultdict(int), '', w, n
		while w > 0 and i > 0:	
			(w, i), j = back[w,i]
			copies[i] = j
		for i in xrange(n):
			selection = selection + str(copies[i])  + ' '
		return selection

	best = search(w, n)
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