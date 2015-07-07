# Find k smallest element in a data stream using heap

from heapq import heappush, heapreplace, heappop, heapify
from sys import stdin

def datastream():
	k, heap = int(stdin.readline()), []
	for line in stdin:
		curr = int(line)
		if len(heap) == k:
			if curr < -heap[0]:
				heapreplace(heap, -curr)
		else:
			heappush(heap, -curr)

	heap = [-x for x in heap]
	heapify(heap)
	while heap:
		print heap[0],
		heappop(heap)

datastream()