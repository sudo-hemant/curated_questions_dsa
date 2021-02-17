

#NOTE: we use the two pointer approach in sorted array, & skip the elements which are repeating

def fourSum(nums, target):
    nums.sort()
    ans = []
    
    for i in range(len(nums) - 3):
        if i != 0 and nums[i] == nums[i-1]:
            continue
        threeSum(nums, i+1, target-nums[i], ans)
    
    return ans

        
def threeSum(nums, start, find, ans):
    first = nums[start-1]
    
    for i in range(start, len(nums) - 2):
        if i != start and nums[i] == nums[i-1]:
            continue
        twoSum(nums, first, i+1, find-nums[i], ans)

    
def twoSum(nums, first, start, find, ans):
    second = nums[start-1]
    low, high = start, len(nums) - 1
    
    while low < high:
        temp = nums[low] + nums[high]
        
        if temp == find:
            ans.append( [first, second, nums[low], nums[high]] )
            low, high = low+1, high-1
            
            while low < high and  nums[low] == nums[low-1]:
                low += 1
            while low < high and nums[high] == nums[high+1]:
                high -= 1
                
        elif temp < find:
            low += 1
            
        elif temp > find:
            high -= 1