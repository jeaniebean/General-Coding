# Find k elements closest to query x in sorted array (using Binary Search)

def _binarysearch(arr, q, low, high): 
    if high < low:
        return high if abs(arr[high]-q) < abs(arr[low] - q) else low
    mid = (high + low) / 2
    return _binarysearch(arr, q, mid+1, high) if arr[mid] < q else _binarysearch(arr, q, low, mid-1) if arr[mid] > q else mid

def find(arr, x, k):
    n = len(arr) - 1
    arr = [float('-inf')] + arr + [float('inf')]
    pivot = _binarysearch(arr, x, 0, n)
    klist, low, high = [arr[pivot]], pivot - 1, pivot + 1
    while len(klist) < k:      
        if abs(arr[low] - x) < abs(arr[high] - x):          
            klist, low = klist + [arr[low]], low - 1
        else:            
            klist, high = klist + [arr[high]], high + 1
    return klist

print ">>>find([1,2,3,4,4,7], 5.2, 2)"      # returns [4,4]
print find([1,2,3,4,4,7], 5.2, 2)

print ">>>find([1,2,3,4,4,7], 6.5, 3)"     # returns [7,4,4]
print find([1,2,3,4,4,7], 6.5, 3)
