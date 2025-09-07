import pandas as pd
import numpy as np

# a
s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([1, 2, 3, 4])

print("Addition:\n", s1 + s2)
print("Subtraction:\n", s1 - s2)
print("Multiplication:\n", s1 * s2)
print("Division:\n", s1 / s2)

# b
data = {'a': 100, 'b': 200, 'c': 300}
series = pd.Series(data)
print(series)

# c
# From list
list_series = pd.Series([1, 2, 3, 4])
print("From list:\n", list_series)

# From NumPy array
array_series = pd.Series(np.array([5, 6, 7, 8]))
print("From NumPy array:\n", array_series)

# From dictionary
dict_series = pd.Series({'x': 9, 'y': 10, 'z': 11})
print("From dictionary:\n", dict_series)

# d
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])

# Vertical stacking (just concatenation)
vertical = pd.concat([s1, s2])
print("Vertical stack:\n", vertical)

# Horizontal stacking (side-by-side as columns)
horizontal = pd.concat([s1, s2], axis=1)
print("Horizontal stack:\n", horizontal)