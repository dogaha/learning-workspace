# priority queue, where elements are popped by priority
# usually implemented as a heap (B tree in form of array)

# Min heap, parent > child
# Max heap, parent < child
# python default is min heap, can use max heap my negating value

# insertion O(logn)
# removal O(logn)

# uses:
# extrat smallest/largest item
# maintaining top k / bottom k set
# real time ranking, greedy selection, ect
# sort on the fly to avoid Onlogn with sort

from heapq import heappop, heappush
def k_closest_point(points: list[list[int]],k:int)->list[list[int]]:
    '''
    Given a list of points.
    find the k closest points to the origin
    '''
    heap:list[tuple[int,list[int]]] = []
    # heaps use first index to sort
    for pt in points:
        heappush(heap,(pt[0]**2+pt[1]**2,pt))
    res = []
    for _ in range(k):
        _,pt = heappop(heap)
        res.append(pt)
    return res

from heapq import heapify
def kth_largest(nums:list[int],k:int)->int:
    '''
    given nums list and k int.
    Find the kth largest value
    '''
    nums = [-x for x in nums]
    heapify(nums)
    for _ in range(k-1):
        heappop(nums)
    return -nums[0]
