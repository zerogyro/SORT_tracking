import numpy as np


x = [748.744,152.562,32.441,55.121]
a = np.array(x)


print(a[2:4])
a[2:4] += a[0:2]
print(a)