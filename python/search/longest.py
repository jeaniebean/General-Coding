# longest path of binary tree

def longest(t):
    length, path, depth, dpath = _longest(t)
    return length, path

def _longest(t):
    # longest path helper function
    if  t == []:
        return 0, [], -1, []

    llength, lpath, ldepth, ldpath = _longest(t[0])
    rlength, rpath, rdepth, rdpath = _longest(t[2])
    length = max(llength, rlength, ldepth+rdepth+1)
    depth, dpath = (ldepth + 1, ldpath + [t[1]]) if ldepth >= rdepth else (rdepth + 1, [t[1]] + rdpath)

    if llength == length:
        return llength, lpath, depth, dpath
    elif rlength == length:
        return rlength, rpath, depth, dpath
    else:
        return ldepth + rdepth + 2, ldpath + [t[1]] + rdpath, depth, dpath
    
print ">>> longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]])"
print longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]])
