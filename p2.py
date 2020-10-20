from scipy.sparse import *
import numpy as np

def p2_has_cycle(sets):
    m=csr_matrix(sets)
    #print(m.todense())
    original=m.copy()
    n=m.shape[0]
    for i in range(n):
        diag=csr_matrix(m.diagonal())
        #print(diag)
        #print(diag.count_nonzero())
        if diag.count_nonzero() != 0:
            return True
        m=original*m
        #print(m.todense())
    return False