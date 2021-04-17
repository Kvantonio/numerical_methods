import numpy as np
import copy


a=[
    [2,1,1,2],
    [1,-1,0,-2],
    [3,-1,2,2]
  ]
#B=[2,-2,2]

def get_free_members(a):
    res = []
    if type(a) is not list:
        a = a.tolist()
    
    for i in range(len(a)):
        if len(a)==len(a[i]):
            res.append(a[i].pop(len(a)-1))
        else:
            res.append(a[i].pop(len(a)))

    return res
    

def kramer(a,r):
    res = []
    
    b=get_free_members(a)
    a = np.array(a)
    a = a.swapaxes(0,1)
    
    s_sav=copy.copy(a)
    determ=np.linalg.det(a)
    if determ == 0:
        return -1    

    for j in range(len(a)):
        a=copy.copy(s_sav)
        a[j]=b
        te=np.linalg.det(a)

        x=te/determ
        res.append(round(x,r))
    return res
    
    

print(kramer(a,5))

    
def gauss():
    pass
