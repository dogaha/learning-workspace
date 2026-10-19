def two_sum(array:list,target:int) -> list:
    # Return Indicies in array that add up target
    # Assume only one solution and cannot use same element twice

    hashmap = {}

    for i,v in enumerate(array):
        diff = target-v
        if diff in hashmap:
            return [hashmap[v],i]
        hashmap[v] = i
        return

def two_pointers_sorted(array):