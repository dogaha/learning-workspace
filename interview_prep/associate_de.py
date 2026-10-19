# Problem 1 — Warm-up (Array/Hash Map)

def my_problem1(nums:list,target:int) -> list:
    hashtable = {value:index for index, value in enumerate(nums)}
    for v1 in nums:
        v2 = target - v1
        if hashtable.get(v2,None) is not None:
            return [hashtable[v1],hashtable[v2]]
    return None

def optimal_my_problem1(nums: list, target: int) -> list:
    seen = {}
    for i, v in enumerate(nums):
        complement = target - v # get complement
        if complement in seen: # DICTS SEARCH IN O(N)
            return [seen[complement], i]
        seen[v] = i # when  add value to key
    return None

# my dumb ass did not read the question correctly
# thought it meant in a row repititions
def my_problem2(s:str)->str:
    longest = ""
    temp = ""
    for index in range(len(s)):
        if temp and temp[len(temp)-1] == s[index]:
            longest = temp if len(temp) > len(longest) else longest
            temp = ""
        temp += s[index]
    return longest

def my_problem2_1(s:str)->str:
    seen = {}
    result = ""
    temp = ""
    for char in s:
        if char in seen:
            result = temp if len(result) < len(temp) else result
            temp = ""
            seen = {}
        seen[char] = 0
        temp += char
    result = temp if len(result) < len(temp) else result
    return result

def optimal_problem2(s:str)->int:
    seen = {}
    left = 0
    max_len = 0
    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right
        max_len = max(max_len,right-left+1)
    return max_len

# Bad Logic: only works fails in situations like this [-2,-1,0,10,11]
def my_problem3(num:list)->list:
    import math
    i = math.floor((len(num)+1)/2)-1
    j = math.ceil((len(num)+1)/2)-1
    result = []

    if i == j:
        result.append(pow(num[i],2))
        i-=1
        j+=1
    for cycle in range(len(num)//2):
        i_val = pow(num[i],2)
        j_val = pow(num[j],2)
        if i_val == j_val:
            result.append(i_val)
            result.append(j_val)
        elif i_val < j_val:
            result.append(i_val)
            result.append(j_val)
        else:
            result.append(j_val)
            result.append(i_val)
        i-=1
        j+=1
    return result

def optimal_problem3_1(num:list)->list:
    n = len(num)
    result = [0]*n
    left,right = 0,n-1
    for index in range(n-1, -1, -1): # edges have the highest value, work backwards
        left_sq = num[left] ** 2
        right_sq = num[right] **2
        if left_sq > right_sq:
            result[index] = left_sq
        else:
            result[index] = right_sq
            right -= 1
    return result
    
def my_problem4(s:str,t:str)->bool:
    if len(s) != len(t):
        return False
    check_dict = {}
    for index in range(len(s)):
        if s[index] in check_dict:
            check_dict[s[index]] += 1
        else:
            check_dict[s[index]] = 1

        if t[index] in check_dict:
            check_dict[t[index]] -= 1
        else:
            check_dict[t[index]] = -1
    return all(val == 0 for val in check_dict.values())

def my_problem5(nums: list, target: int) -> list:
    l, r = 0, len(nums) - 1
    while l < r:
        sum_lr = nums[l] + nums[r]
        if sum_lr == target:
            return [l, r]
        elif sum_lr > target:
            r -= 1
        else:
            l += 1
    return None


# Leet Code 1834
# Why Incorrect?
#   The Question asks to GET THE ORDER
#   NOT TO SIMULATE A PROCESSOR
#   I works, however this is A VERY inefficient system O(N^3) probabl
def getOrder(self, tasks: list[list[int]]) -> list[int]:
    available_tasks = []
    result = []
    time = 1
    p_time = 0
    while len(result) != len(tasks):
        # Queue tasks
        for i in range(len(tasks)):
            if tasks[i][0] == time:
                available_tasks.append((tasks[i],i))
        
        # Wait for processing 
        if p_time != 0:
            time += 1
            p_time -= 1
            continue

        # Pick Quickest Task
        quickest_task_index = None
        for task_index in range(len(available_tasks)):
            if quickest_task_index is None:
                quickest_task_index = task_index
                continue
            if available_tasks[quickest_task_index][0][1] > available_tasks[task_index][0][1]:
                quickest_task_index = task_index
            elif available_tasks[quickest_task_index][0][1] == available_tasks[task_index][0][1]:
                quickest_task_index = task_index if available_tasks[quickest_task_index][1] > available_tasks[task_index][1] else quickest_task_index
        
        # Execute Quickest Task
        if quickest_task_index is not None:
            p_time = available_tasks[quickest_task_index][0][1]
            pop = available_tasks.pop(quickest_task_index)[1]
            result.append(pop)
        
        # increment Time
        time += 1

        # if task is being executed decremetn processing time
        p_time -= 1 if p_time != 0 else 0
    return result

def my_ibm_problem():
    """
    Video Player Simulation
    A video streamin service delivers $n$ numbered packets over time
    Return Earliest time re-buffering begins

    Example:
    arrival Rate = 2
    packets = [1,2,3,4,4,5]
    at time $t = 1$
        Packet 1 and 2 recieved
        P1 plaed
        P2 buffered
    at time $t = 2$
        Packet 2 is played
        Packet 3 and 5 are recieved
    at time $t = 3$
        Packet 3 is played from buffer
        Duplicate packet 4 is recieved and ignored
        Packet 5 is recieved and buffered


    """

if __name__ == "__main__":
    p1_arr = [2,7,11,15]
    p1_target = 9
    p1_solution = my_problem1(p1_arr,p1_target)
    print(p1_solution)

    # abacabcabb
    # bbbbb
    # aabcdef
    print(my_problem2_1("tmmzuxt"))

    #[-4, -1, 0, 3, 10]
    #[-7, -3, 2, 3, 11]
    #[-7, -3, 2, 3, 11, 12]
    print(my_problem3([-2,-1,0,10,11]))

    # s = "anagram", t = "nagaram"
    # s = "rat", t = "car"
    print(my_problem4("rat","car"))

    print(my_problem5(p1_arr,p1_target))
