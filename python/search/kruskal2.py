from collections import defaultdict
from sys import stdin
from time import time
import re

# Kruskal Algorithm (Union-Find Structure)

class UnionFind(object):
#!/usr/bin/env python
 
# UnionFind.py
# Simple unoptimized union-find implementation
# Author: Evan Dempsey <evandempsey@gmail.com>
# Last Modified: 23/Dec/2012
    """Union-Find is a data structure for keeping track
    of partitions of sets into disjoint subsets"""
 
    def __init__(self):
        """Set up leader and group dictionaries"""
        self.leader = {}  # maps member to group leader
        self.group = {}   # maps group leader to set of members
 
    def makeSet(self, elements):
        """Insert elements as new group"""
        assert type(elements) is list
 
        group = set(elements)
        self.group[elements[0]] = group
        for i in group:
            self.leader[i] = elements[0]
 
    def find(self, element):
        """Return the group associated with an element"""
        return self.leader[element]
 
    def union(self, element1, element2):
        """Merge the groups containing two different elements"""
        leader1 = self.leader[element1]
        leader2 = self.leader[element2]
 
        # If both elements are in same group, do nothing
        if leader1 == leader2:
            return
 
        # Otherwise, merge the two groups
        group1 = self.group[leader1]
        group2 = self.group[leader2]
 
        # Swap names if group1 is smaller than group2
        if len(group1) < len(group2):
            element1, leader1, group1, \
                element2, leader2, group2 = \
                element2, leader2, group2, \
                element1, leader1, group1
 
        # Merge group1 with group2, delete group2 and update leaders
        group1 |= group2
        del self.group[leader2]
        for i in group2:
            self.leader[i] = leader1
 
    def getNumGroups(self):
        """Return the number of groups"""
        return len(self.group)
				
def kruskal(graph, capacity, V, src, dest):
	visited, edges, sorted_edges, min_weight = [0]*V, set(), set(), 0
	tree = UnionFind()
	[tree.makeSet([v]) for v in xrange(V)]
	
	for u in graph:
		[edges.add((capacity[u,v], u, v)) for v in graph[u]]
	sorted_edges = sorted(edges)
	edges.clear()
	
	for weight, u, v in sorted_edges:
		if tree.find(u) != tree.find(v):
			u, v = min( (u, v), (v, u) )
			edges.add( (str(u) + '-' + str(v) + ':' + str(weight)))		
			visited[u], min_weight = True, min_weight + weight
			tree.union(u, v)
			
	if len(edges) < dest:
		print 'NO SPANNING TREE'
	else:
		print min_weight, ' '.join( sorted(edges) )

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
		kruskal(graph, capacity, V, src, dest)
		print time() - t

if __name__ == "__main__":
        main()