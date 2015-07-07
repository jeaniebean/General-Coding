import random

# Quickselect with randomized pivot

def qselect(n, t):

    if t == []:
        return []
    else:
        pivot = random.choice(t)
        left = [x for x in t if x < pivot]
        right = [x for x in t if x >= pivot]
        if n <= len(left):          
            return qselect(n, left)
        elif n == len(left) + 1 :
            return pivot
        else:
            return qselect(n-len(left), right)

print ">>> qselect(2, [3, 10, 4, 7, 19])"
print qselect(2, [3, 10, 4, 7, 19])
print ">>> qselect(4, [11, 2, 8, 3])"
print qselect(4, [11, 2, 8, 3])
