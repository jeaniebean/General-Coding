from collections import defaultdict
from heapdict import *
from sys import stdin
from time import time
import re

# Dijkstra Algorithm (Binary Heap)

def dijkstra(graph, capacity, V, src, dest):
	dist, visited, queue = [float('inf')]*V, [0]*V, heapdict()
	queue[src], dist[src], visited[src] = 0, 0, True
		
	while queue:
		u, _ = queue.popitem()	# pop vertex with min distance	
		visited[u] = True	
		for v in graph[u]:
			if not visited[v]:
				queue[v] = dist[v] = min(dist[v], dist[u] + capacity[u,v])
				
	print dist[dest] if dist[dest] < float('inf') else 'UNREACHABLE'

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
			capacity[u, v] = capacity[v, u] = weight
			
		t = time()
		dijkstra(graph, capacity, V, src, dest)
		print time() - t

if __name__ == "__main__":
        main()
	