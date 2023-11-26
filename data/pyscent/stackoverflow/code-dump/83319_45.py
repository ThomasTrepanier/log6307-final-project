import numpy as np

def get_whole_ceil(n,near):
    nn = np.divide(n,np.linspace(1,np.ceil(n/near),int(np.ceil(n/near))))
    return(nn[nn%1==0][-1])

def get_whole_floor(n,near):
    nn = np.divide(n,np.linspace(np.floor(n/near),n,int(n-np.floor(n/near)+1)))
    return(nn[nn%1==0][0])

get_whole_ceil(2040906,1440)

Out[1]: 48593.0

get_whole_floor(2040906,1440)

Out[1]: 42.0
