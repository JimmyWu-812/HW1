from scipy.sparse import *
import numpy as np

def p1_has_cycle(sets):
  m=csr_matrix(sets)
  n=m.shape[0]
  #print(m.todense())
  while True:
    #print(m.shape[0])
    try:
      #csr_matrix
      res=hstack([[[1]]*(n-1),identity(n-1)])*m
      #print(res.todense())
      res2=csr_matrix(res.power(2).sum(axis=1))
      if res2.count_nonzero() != res2.shape[0]:
        return True
      else:
        c1=find(res.T[find(m[0]==-1)[1][0]]==-1)[1]
        c2=find(res2.T==2)[1]
        toBeAppended = res[np.intersect1d(c1,c2),:]
        m=vstack([m,toBeAppended])
        #print(m.todense())
    except:
      return False
    m=m[1:]
    n=m.shape[0]
    #print('-'*40)