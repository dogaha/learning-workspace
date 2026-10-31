# this is similar to two pointers but instead with a range
# the range or "window" will increase/decrease in size as it moves

# Common for aggregations of a subarray

# Types of sliding windows
# Fixed window: size of window is constant
#   Used when given a size
#   EX: find the maximum average of any subarray of size k


# Dynamic Window: Size of window can change
#   Used to when not given a size or tasked to find a size
#   EX: Return the longest window where x rule is valid
#   EX: what is the smallest subarray with a sum greater than target
#   EX: find the length of the longest substring with k unqiue chars


# fixed window example
def subarray_sum_fixed(nums:list[int],k:int) ->int:
    # return the largest sum beween all subarrays k in size
    window_sum = 0
    for i in range(k):
        window_sum += nums[i]
    largest = window_sum
    for right in range(k,len(nums)):
        left = right - k
        window_sum -= nums[left]
        window_sum += nums[right]
        largest = max(largest,window_sum)

    '''Originally i wanted to use sum() but this causes n^2 run time because 
    calculates sum over again'''

# Dynamic  Window example
from collections import defaultdict
def longest_unique_char_substring(s: str) -> int:
    '''
    Return then length of the largest substring with no repeating chars
    '''
    longest = 0
    left = 0
    counter: dict[str,int] = defaultdict(int)
    for right in range(len(s)):
        counter[s[right]]  += 1
        while counter[s[right]] > 1:
            counter[s[left]] -= 1
            left += 1
        longest = max(longest, right - left + 1)
    return longest


