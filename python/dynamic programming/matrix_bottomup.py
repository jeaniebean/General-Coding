from collections import defaultdict
from sys import stdin

# Matrix Chain Multiply (Bottom-Up)

def matrix_chain(m):
   opt, back, len_m = defaultdict(lambda: float('inf')), defaultdict(int), len(m)    

   for i in xrange(1, len_m + 1):
      opt[i, i] = 0

   for L in xrange(2, len_m + 1):
      for i in xrange(1, len_m - L + 2):
         j = i + L -1
         for k in xrange(i, j):
            (start, _), (_, mid), (_, end) = m[i], m[k], m[j]
            sub = opt[i, k] + opt[k+1, j] + start*mid*end
            opt[i,j], back[i,j] = min( (opt[i,j], back[i,j]) , (sub, k) )

   def backtrace(i,j):
      if i == j:
         return 'A' + str(i)
      k = back[i,j]
      return '(' + backtrace(i, k) + backtrace(k+1, j) + ')'

   min_size =  opt[1, len_m]
   chain_order = backtrace(1, len_m)
   print min_size, chain_order

def main():
   N = int(stdin.readline())
   for _ in xrange(N):
      m = {}
      chain = stdin.readline().split()
      for i, size in enumerate(chain, 1):
         row, col = map(int, size.split('x'))
         m[i] = (row, col)
      matrix_chain(m)

if __name__ == "__main__":
        main()



'''input : 
2
1x2 2x5 5x1
30x35 35x15 15x5 5x10 10x20 20x25
'''