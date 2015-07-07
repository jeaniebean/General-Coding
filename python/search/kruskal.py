from collections import defaultdict
from sys import stdin
from time import time
import re

# Kruskal Algorithm (Naive Coloring)

def kruskal(graph, capacity, V, src, dest):
	visited, edges, sorted_edges, min_weight = [0]*V, set(), set(), 0
	colors = [v for v in xrange(V)]

	def cyclic(_u, _v): 
		if colors[_u] == colors[_v]: return True		
		_old, _new = min(colors[_u], colors[_v]), max(colors[_u], colors[_v]) 
		for i, color in enumerate(colors):
			if color == _old: 
				colors[i] = _new
		return False
	
	for u in graph:
		[edges.add((capacity[u,v], u, v)) for v in graph[u]]
	sorted_edges = sorted(edges)
	edges.clear()
	
	for weight, u, v in sorted_edges:
		if (u,v) not in edges and (v,u) not in edges:
			if not cyclic(u, v):
				min_weight, (u, v) = min_weight + weight, min((u,v), (v,u))
				edges.add( (str(u) + '-' + str(v) + ':' + str(weight)))	
				visited[u] = visited[v] = True
		
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
			capacity[u,v] = capacity[v,u] = weight
			
		t = time()
		kruskal(graph, capacity, V, src, dest)
		print time() - t

if __name__ == "__main__":
        main()
	