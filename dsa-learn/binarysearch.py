# seach for a number in log(n) time given that it is sorted
# the idea is to cut the options in half

# binary serarch template
def binary_serach(arr:list[int],target:int) -> int:
    left, right = 0, len(arr) -1
    while left<=right:
        mid = (left+right) //2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid + 1
    return -1

# CORRECTION you DONT need a SORTED array
# you only need the CONDITION to be monotonic: it only changes in one direction
#   EX: only increases, never decreases / Only decreases @ point
# This is important because this will apply to non int tables
#   EX: given table of F and T, you can find the first T with BS
#       F F F T T T T
#   The template conditions changes to a feasiblility check

def find_boundary(arr:list[bool]) -> int:
    '''
    Given a boolean array, where all the falses are on left and trues on right.
    Find the index of the first true
    '''
    left,right = 0, len(arr)-1
    boundary_index = -1 # need this in case of all False arr
    while left <= right: # loop will continue until the left <= right, no breaks
        mid = (left+right) // 2
        if arr[mid]:
            boundary_index = mid 
            right = mid - 1
        else:
            left = mid + 1
    return boundary_index

def find_min_rotated(arr:list[int])->int:
    '''
    Given an array that was previously sorted but then rotated at some pivot.
    Find the index of the minimum element
    EX: [10,20,30,40,50] -> [40,50,10,20,30] = output 3
    '''
    left, right = 0, len(arr)-1
    boundary_index = -1
    while left <= right:
        mid = (left+right) // 2
        # at the pivot, all values to the left are > right
        if arr[mid] <= arr[-1]:
            boundary_index = mid
            right = mid -1
        else:
            left = mid + 1
    return boundary_index