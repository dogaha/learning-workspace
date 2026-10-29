# a way to store data using a key and value
# unordered 
# runs in O(1), hashfunction will return value based on key
# collsion is when two keys ge the same hash, dont need to worry

# Keys must be "hashable", must be constant / immuteable
# Numbers, strings, tuples = hashable
# lists and dicts/hashmaps = not haseable

# why popular
# goto for when brute force is too slow
# Finding a value when too slow, O(n) search vs O(1) search


# hashmap flow
# 1. store something
# 2. look something up
# 3. update / initalize values

# use cases
# extremely flexible
# used in literally everything
# have i seen this before?

# ask what can i store that i will need later


def frequency_map(data:list) -> dict:
    my_map = {}
    for item in data:
        if item not in my_map:
            my_map[item] = 1
        else:
            my_map[item] += 1
    return my_map


def two_sum(nums:list,target:int) -> list:
    # return the two indexes in nums that add up to target
    # assume that there is exactly one solution

    # target - value = value in list
    my_map = {}
    for i,v in enumerate(nums):
        complement = target - v
        if complement in my_map:
            return [my_map[complement],i]
        my_map[complement] = i
    return []