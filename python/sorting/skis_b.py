def skis_b():
	n_len, q = map(int, raw_input().split())
	n = map(int, raw_input().split())
	n.sort()
	left, right, pairs = 0, n_len-1, 0

	while left < right:
		s = n[left] + n[right]
		if  s < q:
			left += 1
		elif s > q:
			right -= 1
		else:
			left, right, pairs = left+1, right-1, pairs+1

	return pairs

print skis_b()
