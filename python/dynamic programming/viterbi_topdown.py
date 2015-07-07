from collections import defaultdict
from sys import stdin

# Viterbi Algorithm (Top-Down)

def viterbi(unordered_graph, V):

	def top_sort():
		adj_in, adj_out = defaultdict(list), defaultdict(list)
		in_deg = {i: 0 for i in xrange(1, V+1)}
		ordered_graph, zero_list = [], []

		for (u, v) in unordered_graph:
			adj_in[v].append(u)
			adj_out[u].append(v)
			in_deg[v] += 1

 		while len(ordered_graph) < V:
 			removed = 0

 			for node in in_deg:
 				if not (in_deg[node] or node in zero_list):
 					ordered_graph.append(node)
 					zero_list.append(node)
 					removed += 1
	 				for adj in adj_out[node]:
						in_deg[adj] -= 1
 			if not removed:
 				return [], []

 		return ordered_graph, adj_in

 	ordered_graph, adj_matrix = top_sort()

 	opt = defaultdict(int)
	def search(v):
		if v not in opt:
			if v == 1:
				opt[v] = 1
			else:
				for u in adj_matrix[v]:
					opt[v] += search(u)
		return opt[v]

 	if not ordered_graph:
 		return 'CYCLIC'
	return search(V)

def main():
	n = int(stdin.readline())
	
	for _ in xrange(n):
		V, E = map(int, stdin.readline().split())
		edges = map(lambda x: x.strip('(,)'), stdin.readline().split())

		G, i = [], 0;
		for _ in xrange(E):
			u, v, i = int(edges[i]), int(edges[i+1]), i+2
			G.append((u,v))

		print viterbi(G, V)

if __name__ == "__main__":
        main()
	
'''input : 
2
5 6
(1, 2) (1, 3) (3, 2) (2, 5) (3, 5) (5, 4)
3 3
(1, 2) (2, 3) (3, 2)
'''