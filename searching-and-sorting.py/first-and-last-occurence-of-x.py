
# TODO: have a look at the 2nd method given in leetcode
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/

# TODO: how this binary search is finding desired output in this much less code
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14701/A-very-simple-Java-solution-with-only-one-binary-search-algorithm


def searchRange(nums, target):
    first = firstOccurence(nums, target)
    
    if first == -1:
        return [-1, -1]
    if first == len(nums) - 1:
        return [first, first]
    
    last = lastOccurence(nums, first, target)
    return [first, last]
    

def firstOccurence( nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if mid == 0 and nums[mid] == target:
            return mid
                        
        if nums[mid] == target:
            if nums[mid - 1] == target:
                r = mid - 1
            else:
                return mid
        elif target < nums[mid]:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
            
    return -1


def lastOccurence( nums, start, target):
    l, r = start, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if mid == len(nums) - 1 and nums[mid] == target:
            return mid
        
        if nums[mid] == target:
            if nums[mid + 1] == target:
                l = mid + 1
            else:
                return mid
        elif target < nums[mid]:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
            
    return -1



# ----------------------------------------------------------


