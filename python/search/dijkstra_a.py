from collections import defaultdict
from sys import stdin
from time import time
import re

# Dijkstra Algorithm (Array)

def dijkstra(graph, capacity, V, src, dest):
	dist, visited = [float('inf')]*V, [0]*V
	dist[src] = 0
	
	while True:
		u, shortest = -1, float('inf')
		for v in xrange(V):
			if not visited[v] and dist[v] < shortest:
				u, shortest = v, dist[v]
		if shortest == float('inf'): break
		
		for v in graph[u]:
			if not visited[v]:
				dist[v] = min(dist[v], dist[u] + capacity[u,v])
		visited[u] = True
			
	print dist[V-1] if dist[V-1] < float('inf') else 'UNREACHABLE'

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
	