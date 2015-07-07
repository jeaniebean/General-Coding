# Ackerman Function

def A(m, n):
    # naive ackermann
    if m == 0:
        return n+1
    elif n == 0:
        return A(m-1, 1)
    else:
        return A(m-1, A(m, n-1))

def A2(m, n, cache={}):
    # memoized ackermann
    if (m,n) not in cache:
	cache[m,n] = n+1 if m == 0 else (A2(m-1,1) if n == 0 else A2(m-1, A2(m, n-1)))
    return cache[m,n]

def A3(m, n):
    if m == 0 :
        print "A(%d,%d)" % (m, n+1)
    elif n == 0 :
        print "A(%d," % (m-1),
    else :
        print "A(%d, A(%d, %d))" % (m-1, m, n-1)
    if m == 0:      
        return n + 1
    elif n == 0:          
        return A3(m-1, 1)
    else:             
        return A3(m-1, A3(m, n-1))

#print ">>> import sys; sys.setrecursionlimit(1000000)"
import sys; sys.setrecursionlimit(1000000)

print ">>> A(3,10)"
print A(3,10)
print ">>> A2(3,10)"
print A2(3,10)
print ">>> A(4,0)"
print A(4,0)
print ">>> A2(4,1)"
print A2(4,1)
print
print
print "non-cached trace"
print ">>>A3(2,1)"
print A3(2,1)




