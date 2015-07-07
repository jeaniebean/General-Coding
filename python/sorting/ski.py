'''
A warehouse of the oldest sports shop of Berland received n skis, the length of the i-th ski equals ai centimeters. Your task is to find out the largest number of ski packs to sell if a ski pack must contain two skis and the sum of their lengths must equal exactly q centimeters. Note that the Berland skis aren't differentiated as left or right.

Input
The first line contains two positive integers n and q. The second line contains n positive integers a1, a2, ..., an (1 ≤ ai ≤ q).

Limits n and q are distinct for distinct problems:

for subproblem A1: 1 ≤ n, q ≤ 100,
for subproblem A2: 1 ≤ n, q ≤ 106.
Output
Print the required maximum number of packs.

input 
7 5
1 2 1 4 3 1 3

output 2
'''

def ski_ver1():
	n_len, q = map(int, stdin.readline().split())
	n = map(int, stdin.readline().split())
	arr, mid = [0]*(q+1), (q+1)/2
	for i in n:
		arr[i] += 1

	pairs = arr[q/2]/2 if not q%2 else 0
	for i in range(mid):
		pairs += min(arr[i], arr[q-i])

	return pairs

def ski_ver2():
	n_len, q = map(int, stdin.readline().split())
	n = map(int, stdin.readline().split())

	table, mid = {}, (q+1)/2
	for i in n:
	    table[i] = 1 if i not in table else table[i] + 1

	pairs = table[q/2]/2 if q%2 == 0 and q/2 in table else 0
	for i in range(mid):
		if i in table and q - i in table:		
			pairs += min(table[i], table[q-i])

	return pairs

def ski_ver3():
	n_len, q = map(int, stdin.readline().split())
	n = map(int, stdin.readline().split())
	n.sort()
	left, right, pairs = 0, n_len-1, 0

	while left < right:
		s = n[left] + n[right]
		if  s == q:
			left, right, pairs = left+1, right-1, pairs+1
		elif s < q:
			left += 1
		else:
			right -= 1

	return pairs


def run():
	n, q = map(int, stdin.readline().split())
	nset = map(int, stdin.readline().split())

	print ski_ver1(q, nset)
	print ski_ver2(q, nset)
	print ski_ver3(q, nset, n)

run()
