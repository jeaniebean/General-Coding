def _longest(tree):
    '''return a quadruple: (max-length, longest-path, max-depth, deepest-path, deepest-path-reversed)'''
    ' revised from the solution posted on the website'
    if tree == []:
        return 0, [], -1, [], []
    left, root, right = tree
    l1, lp1, d1, dp1, dpr1 = _longest(left)
    l2, lp2, d2, dp2, dpr2 = _longest(right)
    d = max(d1, d2) + 1
    dp = (dp1 if d1 >= d2 else dp2) + [root]
    dpr = [root] + dpr1 if d1 >= d2 else [root] + dpr2
    if d1 + d2 + 2 > max(l1, l2):
        return d1 + d2 + 2, dp1 + [root] + dpr2, d, dp, dpr
    elif l1 >= l2:
        return l1, lp1, d, dp, dpr
    return l2, lp2, d, dp, dpr

def longest(tree):
    return _longest(tree)[:2]

print longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]])
print longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[[], 9, []], 5, []], 6, [[], 7, []]]])