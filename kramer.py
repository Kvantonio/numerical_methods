import numpy as np
import copy


def kramer(A,B,rd):
    res = []
    
    A = np.array(A)
    A = A.swapaxes(0,1)
    
    s_sav=copy.copy(A)
    determ=np.linalg.det(A)
    if determ == 0:
        return -1    

    for j in range(len(A)):
        A=copy.copy(s_sav)
        A[j]=B
        te=np.linalg.det(A)
        x=te/determ
        res.append(round(x,rd))

    return res
