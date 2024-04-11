# ValueError: all the input array dimensions for the concatenation axis must match exactly

import numpy as np

arr1 = np.array([[1, 2, 3]])
arr2 = np.array([[4, 5, 6]])

print(arr1.shape)  # (1, 3)
print(arr2.shape)  # (1, 3)


new_arr = np.concatenate((arr1, arr2))

# [[1 2 3]
#  [4 5 6]]
print(new_arr)