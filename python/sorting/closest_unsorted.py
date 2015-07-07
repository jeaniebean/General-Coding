# Find k elements closest to query x in unsorted array (using quick select)

import random

def _qselect(n, a):
    if a == []:
        return []
    pivot = random.randint(0, len(a)-1)
    left = [x for x in a if x < a[pivot]]
    left_len = len(left)
    
    if n <= left_len:
        return _qselect(n, left)
    elif n == left_len + 1:
        return a[pivot]
    else:
        right = [y for y in a[:pivot]+a[pivot+1:] if y >= a[pivot]]
        return _qselect(n-left_len-1, right)

def find(arr, x, k):
    new_arr = [(abs(x-y), i) for i, y in enumerate(arr)]
    pivot = _qselect(k, new_arr)
    return [arr[y] for x,y in new_arr if x <= pivot[0]]


print ">>>find([4,1,3,2,7,4], 5.2, 2)"      # returns [4,4]
print find([4,1,3,2,7,4], 5.2, 2)

print ">>>find([4,1,3,2,7,4], 6.5, 3)"     # returns [4,7,4]
print find([4,1,3,2,7,4], 6.5, 3)
