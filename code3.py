import numpy as np
import time
from numba import jit
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
C = np.random.rand(10000, 10000)
D = np.random.rand(10000, 10000)

def plus_matrix_without_parallelism(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

for i in range(1,10):
    init= time.time()
    plus_matrix_without_parallelism(A, B)
    print('Time without parallelism',time.time()-init)


@jit(nopython=True, parallel=True)
def plus_matrix_with_parallelism(C, D):
    return C + D

print('\n')
for i in range(1,10):
    init= time.time()
    plus_matrix_with_parallelism(C, D)
    print('Time with parallelism',time.time()-init)