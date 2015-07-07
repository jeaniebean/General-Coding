# Merge Sort

def mergesorted(a, b):
    if a == [] or b == []:
        return a + b
    if a[0] < b[0]:
        return [a[0]] + mergesorted(a[1:], b)
    return [b[0]] + mergesorted(b[1:], a)

def mergesort(a):
    if len(a) < 2:
        return a
    left, right = mergesort(a[:len(a)/2]), mergesort(a[len(a)/2:])
    return mergesorted(left, right)
