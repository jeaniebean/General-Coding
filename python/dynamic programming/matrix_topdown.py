from collections import defaultdict
from sys import stdin

# Matrix Chain Multiply (Top-Down)

def matrix_chain(m):
   opt, back, len_m = defaultdict(lambda: float('inf')), defaultdict(int), len(m)    

   def optimize(i, j):
      if (i,j) not in opt:
         if i == j:
            opt[i,j] = 0
         else:
            (start, _), (_, end) = m[i], m[j]
            for k in xrange(i, j):
               _, col = m[k]
               sub = optimize(i,k) + optimize(k+1, j) + start*col*end
               opt[i,j], back[i,j] = min( (opt[i,j], back[i,j]) , (sub, k) )
            
      return opt[i,j]

   def backtrace(i,j):
      if i == j:
         return 'A' + str(i)
      k = back[i,j]
      return '(' + backtrace(i, k) + backtrace(k+1, j) + ')'

   min_size = optimize(1, len_m)
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