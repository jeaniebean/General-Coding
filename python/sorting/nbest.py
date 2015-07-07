import random
import time
from heapq import heappop, heappush

# Select n smallest elements from the enumeration of given two lists.

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

def nbesta(a, b):
	# enumerate both lists, sort, select top n values.
    c =  sorted( [(x + y, y, x) for x in a for y in b])
    return [(z,y) for _,y,z in c][:len(a)]

def nbestb(a, b):
	# enumerate both list, quick select top n values.
    c, n = [(x+y, y, x) for x in a for y in b], len(a)
    pivot, y, x = _qselect(n, c)
    c1 = sorted( [(x,y,z) for (x,y,z) in c if x < pivot] )
    c1 = c1 + sorted( [(x,y,z) for (x,y,z) in c if x == pivot] ) if len(c1) < n else c1
    return [(z,y) for _,y,z in c1][:n]

def nbestc(a, b):
	# Dijkstra style best first, enumerate n sums.
    a, b, c, heap = sorted(a), sorted(b), [], []
    i, j, n, hmap = 0, 0, len(a), {}
    heappush( heap, (a[i]+b[j], b[j], a[i],  i, j) )
    while len(c) < n:
        x, y, z, i, j = heappop(heap)
        c.append( (x, y, z) )
        if (i+1, j) not in hmap:
            hmap[(i+1, j)] = a[i+1] + b[j]
            heappush( heap, (a[i+1] + b[j], b[j], a[i+1], i+1, j) )      
        if (i, j+1) not in hmap:
            hmap[(i, j+1)] = a[i] + b[j+1]
            heappush( heap, (a[i] + b[j+1], b[j+1], a[i], i, j+1) )
    return [(z,y) for _,y,z in c]

def timing(n):
    a = [random.randint(0, 100) for _ in xrange(n)]
    b = [random.randint(0, 100) for _ in xrange(n)]

    print "Randomly generated list of ", n, "numbers"
    
    t = time.time(); ca = nbesta(a, b)
    print "Algorithm time of nbesta :", time.time() - t
    t = time.time(); cb = nbestb(a, b)
    print "Algorithm time of nbestb :", time.time() - t
    t = time.time(); cc = nbestc(a, b)
    print "Algorithm time of nbestc :", time.time() - t

    print "All lists are equal : ", ca == cb == cc

def test():
    print '>>> a, b = [4, 1, 5, 3], [2, 6, 3, 4]'
    a, b = [4, 1, 5, 3], [2, 6, 3, 4]
    t = time.time(); nbesta(a, b)
    print "Algorithm time of nbesta :", time.time() - t
    t = time.time(); nbestb(a, b)
    print "Algorithm time of nbestb :", time.time() - t
    t = time.time(); nbestc(a, b)
    print "Algorithm time of nbestc :", time.time() - t

    timing(1000)
    timing(3000)
    timing(5000)

test()
