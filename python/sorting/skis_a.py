import sys; from sys import stdin

def skis_a():
	n_len, q = map(int, stdin.readline().split())
	n = map(int, stdin.readline().split())

	table, mid = {}, (q+1)/2
	for i in n:
	    table[i] = 1 if i not in table else table[i] + 1

	pairs = table[q/2]/2 if q%2 == 0 and q/2 in table else 0
	for key in table:
		if key < mid and q-i in table:		
			pairs += min(table[i], table[q-i])

	return pairs

print skis_a()