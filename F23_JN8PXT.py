import numpy as np

def ossz(m):
    a = m.size
    kov = []
    for i in m:
        if a - i > 0:
            kov.append(a-i)
    return sum(kov) % (10**9 + 7)

m = np.array([1, 2, 3, 4, 5])
print(ossz(m))