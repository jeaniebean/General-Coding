from collections import defaultdict
from heapdict import *
from sys import stdin
from time import time
import re

# Prim Algorithm (Binary Heap)

def prim(graph, capacity, V, src, dest):
	dist, visited, prev = [float('inf')]*V, [0]*V, [-1]*V
	queue, edges = heapdict(), set()
	min_weight, queue[src], dist[src], visited[src] = 0, 0, 0, True

	while queue:
		u, weight = queue.popitem()
		visited[u] = True
		if weight:
			min_weight, (_u, _v) = min_weight + weight, min( (prev[u], u), (u, prev[u]))
			edges.add( (str(_u) + '-' + str(_v) + ':' + str(weight)) )	
		for v in graph[u]:
			if not visited[v]:
				dist[v], prev[v] = min( (dist[v], prev[v]), (capacity[u, v], u))
				queue[v] = dist[v]
	
	if len(edges) < dest:
		print 'NO SPANNING TREE'
	else:
		print min_weight, ' '.join(sorted(edges))

def main():

	while True:
		V, E = map(int, stdin.readline().split())
		if V == -1 and E == -1: break
		
		edges = stdin.readline().split()
		graph, capacity, src, dest = defaultdict(list), {}, 0, V-1
		for edge in edges:
			u, v, weight = map(int, re.split('[-:]+', edge) )
			graph[u].append(v)
			graph[v].append(u)
			capacity[u,v ] = capacity[v, u] = weight
			
		t = time()
		prim(graph, capacity, V, src, dest)
		print time() - t

if __name__ == "__main__":
        main()
	