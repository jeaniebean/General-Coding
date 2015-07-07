from heapq import heappop, heappush
import sys; sys.setrecursionlimit(1000000000)

# K-way merge sort

def kmergesort(arr, k):
	arr_size = len(arr)
	if arr_size < k:
		return sorted(arr)
	else:
		step, r = arr_size / k, arr_size % k
		l_part = step + r
		stop = arr_size if r == 0 else (arr_size - l_part)
		sub_arr = [kmergesort(arr[i:i+step], k) for i in xrange(0, stop, step)]
		if stop < arr_size:
			sub_arr.append( kmergesort(arr[-l_part:],k) )
		a = _kmerge(sub_arr, k)
		return a

def _kmerge(arr, k):
	if len(arr) == k:
		heap, sorted_arr = [], []
		for i, sub_arr in enumerate(arr):
			heappush(heap,(sub_arr[0], sub_arr))	
		while heap:
			_min, curr_arr = heappop(heap)
			sorted_arr.append(_min)
			curr_arr.remove(_min)	
			if curr_arr != []:
				heappush(heap,(curr_arr[0], curr_arr))
		return sorted_arr
	return arr

print ">>> kmergesort([4,1,5,2,6,3,7,0], 3)"
print kmergesort([4,1,5,2,6,3,7,0], 3) 




