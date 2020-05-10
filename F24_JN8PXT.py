import numpy as np

def rendezes(v):
    j = 0
    tmp1_v = np.array([])
    tmp2_v = np.array([])
    for i in range(0, len(v)):
        if v[i] == -1:
            pass
        else:
            tmp1_v = np.append(tmp1_v, v[i])
    
    tmp1_v = np.sort(tmp1_v)
    
    for i in range(0,len(v)):
        if v[i] == -1:
            tmp2_v = np.append(tmp2_v, v[i])
        else:
            tmp2_v = np.append(tmp2_v, tmp1_v[j])
            j += 1
            
    return tmp2_v


v = np.array([-1, 150, 190, 170, -1, -1, 160, 180])
print(rendezes(v))