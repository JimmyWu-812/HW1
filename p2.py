from scipy.sparse import *
import numpy as np

def p2_has_cycle(sets):
    m=csr_matrix(sets)
    #print(m.todense())
    original=m.copy()
    n=m.shape[0]
    i=0
    while i<n:
        diag=csr_matrix(m.diagonal())
        #print(diag)
        #print(diag.count_nonzero())
        if diag.count_nonzero() != 0:
            return True
        m=original*m
        i+=1
        #print(m.todense())
    return False