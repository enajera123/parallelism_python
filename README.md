# Parallel Bubble Sort in Python

A demonstration of bubble sort implementation with and without multiprocessing.

## Code

```python
from multiprocessing import Process
import time

def bubble_sort(array):
    check = True
    while check:
        check = False
        for i in range(0, len(array)-1):
            if array[i] > array[i+1]:
                check = True
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp

def call_bubble_sort(array):
    init = time.time()
    bubble_sort(array)
    print('Time without parallelism:', time.time() - init)

def call_bubble_sort_parallel(array):
    init = time.time()
    p = Process(target=bubble_sort, args=(array,))
    p.start()
    p.join()
    print('Time with parallelism:', time.time() - init)

if __name__ == '__main__':
    array = list(range(10000000, 1, -1))  # Large reverse-sorted array
    call_bubble_sort_parallel(array.copy())
    call_bubble_sort(array.copy())
