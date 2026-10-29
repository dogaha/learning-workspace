# using two pointers to read two values at once

# Types of Pointers
# Same direction
# slow pointer and fast pointer
# this allows for you to find the middle and cycle

# Opposite Direction
# Left pointer @ 0, Right pointer at n-1
# move pointer(s) based on some condition

def is_palindrome_limited(s:str)->bool:
    # assuming that only alphabetical 
    l = 0
    r = len(s) - 1
    while (l<r): # continue if l > r (crossed) or l = r
        if s[l] != s[r]:
            return False
        l+=1
        r-=1
    return True

def is_palindrome_unlimited(s:str)->bool:
    # assuming any char
    # consider alphanumeric and ignore case
    l = 0
    r = len(s) - 1
    while (l<r): # continue if l > r (crossed) or l = r
        while l<r and not s[l].isalnum(): # keep incrementing until reach letter or cross
            l+=1
        while l<r and not s[r].isalnum(): # keep incrementing until reach letter or cross
            r-=1
        if s[l].lower() != s[r].lower():
            return False
        l+=1
        r-=1
    return True

# linked list
class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

def middle_linked_list(head:Node)->int:
    # get tha value of  the halfway point of a linked list
    # If even point to the lower half

    slow = fast = head
    # idea increment one pointer double the other
    # this means that the slow pointer will always point to 1/2 of the fast
    # thus once the fast reaches the end, the slow will point to the middle
    # this works with odd length too because even though it does not reach
    # the end exactly, odd number midpoint is n+1/2, which matches lower even
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val

if __name__ == "__main__":
    s ="racecarss"
    print(is_palindrome_limited(s))