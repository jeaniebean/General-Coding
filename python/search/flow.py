from collections import defaultdict
from sys import stdin
import re

# Max Flow (Edmond Karp)

def edmond_karp(graph, capacity, V, src, dest):
	flows, maxflow = defaultdict(int), 0
	
	def _path():	#DFS of augmented path
		prev, max_flow, queue = [-1]*V, [0]*V, [src]
		prev[src] = max_flow[src] = float('inf')
		
		while queue:
			u = queue.pop(0)
			for v in graph[u]:
				if capacity[u,v] - flows[u,v] and prev[v] == -1:
					prev[v] = u
					max_flow[v] = min(max_flow[u], capacity[u,v] - flows[u,v])
					if v == dest:
						return max_flow[dest], prev
					else:
						queue += [v]
		return 0, prev
	
	while True:
		residual, prev = _path()
		if residual == 0: break
		u, v, maxflow = prev[dest], dest, maxflow + residual
		while v != src:
			if v in graph[u]:
				flows[u,v] += residual
			else:
				flows[v,u] -= residual
			u, v = prev[v], u
		
	if not flows[src, dest]:
		print 'NO FLOW'
	else:
		edge = set()
		for flow in flows:
			u, v = flow
			if flows[u, v] > 0:
				u, v = min( (u,v), (v,u) )
				edge.add(str(u) + '-' + str(v) + ':' + str(flows[flow]) + ' ')
		print flows[src, dest], ''.join(sorted(edge))
	
def main():

	while True:
		V, E = map(int, stdin.readline().split())
		if V == -1 and E == -1: break
		
		edges = stdin.readline().split()
		graph, capacity, src, dest = defaultdict(list), defaultdict(int), 0, V-1
		for edge in edges:
			u, v, flow = map(int, re.split('[-:]+', edge) )
			graph[u].append(v)
			capacity[u,v] = flow
			
		edmond_karp(graph, capacity, V, src, dest)

if __name__ == "__main__":
        main()
	