# a
import numpy as np

matrix = np.arange(2, 11).reshape(3, 3)
print(matrix)

# b
arr = np.array([1, 2, 3, 4, 5])
reversed_arr = arr[::-1]
print(reversed_arr)

# c
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
common = np.intersect1d(arr1, arr2)
print(common)

# d
arr = np.array([1, 2, 3])
repeated = np.repeat(arr, 2)  # repeats each element twice
print(repeated)

# e
arr = np.array([1, 2, 3, 4, 5])
memory_size = arr.nbytes
print(f"Memory size: {memory_size} bytes")

# f
zeros = np.zeros((2, 3))  # 2x3 array of zeros
ones = np.ones((2, 3))    # 2x3 array of ones
print("Zeros:\n", zeros)
print("Ones:\n", ones)

# g
arr = np.array([10, 20, 30, 40, 50])
fourth_element = arr[3]  # Indexing starts at 0
print(f"4th element: {fourth_element}")