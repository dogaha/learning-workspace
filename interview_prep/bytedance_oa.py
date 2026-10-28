# Table of Contents
# 1. Data Manipulation
# - NumPy Fundamentals
# - Pandas
# 2. SQL & Query Engine Logic
# - Window Functions
# - Advance Joins
# - Aggregation Filtering
# - Date/Time Math
# 3. DSA
# - HashMaps
# - Two Pointers
# - Sliding Window
# - Prefix Sums
# 4. MCQs
# - Time Complexity
# - Output Tracing
# - DSA Protperties


# Data Manipulatoion

# Numpy Fundamentals:
import numpy as np
arr = np.array([[1, 5, 3],
              [4, 2, 9]])        # shape (2, 3)

# Aggregrations
np.sum(arr,axis=0)
np.mean(arr,axis=0)
np.max(arr,axis=0)
np.min(arr,axis=0)
np.var(arr,axis=0)
np.std(arr,axis=0)

# Masking and Where
arr[arr>3] # create a new 1D array where value > 3
arr[arr>3].sum() # sum all the values where value > 3
np.where(arr > 3,1,0) # places 1 where value > 3, and 0 else
np.where(arr > 3) # return two arrays one holding row and other col for position
((arr > 1) & (arr < 5)).sum # counts all the values where x is 1<x<5

# Indexing
arr[1,2] # row 1, column 2
arr[:,0] # get column 0
arr[0] # get row 0
arr[:,[0,2]] # get columns 0 AND 2
arr[::-1] # reverse array row elemenets
arr.argmax(axis=1) # returns the index of each max value in rows

# Shape and broadcasting
arr.reshape(3,2) # fills out new matrix by row: note size must equal
arr.T # transpose matrix
arr - arr.mean(axis=0) # subtract the mean by column
arr - arr.mean(axis=1) # subtract the mean by row BUT WILL GET ERROR because size 2 does not divde into 3 well
arr - arr.mean(axis=1, keepdims=True) #keep dims maintains dimension allowing size (2,1) *use right does and 1 can spread into 3

# Sort, Unique, Cumulative
np.sort(arr, axis=1) # sorts the rows 
arr[np.argsort(arr[:,0])] # first get the first column, next sub it
vals,cnts = np.unique(x, return_counts=True)
np.cumsum(x)
np.diff(x)

# np array conversions
arr1 = np.arr([1,2,3])
arr1.tolist()

# Pandas

# SQL
