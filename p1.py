from scipy.sparse import *
import numpy as np
def p1_has_cycle(sets):
  m=csr_matrix(sets)
  while m.shape[0] > 1:
    #print(m.todense())
    #print(m.shape[0])
    cond1=find(m.T[find(m[0]==1)[1][0]]==-1)[1]
    #print(f"cond1: {cond1}")
    cond2=find(m.T[find(m[0]==-1)[1][0]]==1)[1]
    #print(cond2)
    #print(np.intersect1d(rewireable, match).size)
    if np.intersect1d(cond1, cond2).size != 0:
      return True
    elif cond1.size != 0:
      v=vstack([m[0], m[cond1]])
      #print(cond1)
      toBeAppended2 = hstack([csr_matrix([[1]]*(v.shape[0]-1)), csr_matrix(identity(v.shape[0]-1))])*v
      m=vstack([m, toBeAppended2])
    m=m[1:]
    #print(m.todense())
    #print('-'*40)
  return False
'''
#Older version:
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
    '''