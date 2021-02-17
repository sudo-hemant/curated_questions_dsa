

# NOTE: the problem with the approach of using map is, 
# for ex : lets suppose we are looking for a value x in dict,
# it might have occured twice but we added it only once, so 
# it ll only increase the count by 1 instead of 2 etc..
# hence this APPROACH WILL FAIL 

# NOTE: this is wrong solution, 

def subarray_sum(nums, k):
    
    mp = {}
    curr_sum = 0
    count = 0   

    for i in range(len(nums)):
        curr_sum += nums[i]
        
        if curr_sum == k:
            count += 1
        elif curr_sum > k:
            to_find = curr_sum - k
            if to_find in mp:
                count += 1
        mp[curr_sum] = i

    return count

# ------------------------------------------------

# NOTE: THIS IS CORRECT SOLUTION

from collections import defaultdict

def subarray_sum_count(nums, k):

    dic = defaultdict(int)
    count = 0
    curr_sum = 0

    for i in range(len(nums)):
        curr_sum += nums[i]

        if curr_sum == k:
            count += 1

        #NOTE:   we are not using elif bcos, ex: [1, -1, 0] if we ll use elif  
        # our op ll be 2 but the correct ans is 3
        
        if curr_sum - k in dic:
            count += dic[curr_sum - k]
        
        dic[curr_sum] += 1

    return count


print(subarray_sum_count( [1, -1, 0], 0 ))


# NOTE: Or we can do this

def second_method(nums, k):

    dic = defaultdict(int)
    dic[0] = 1
    count = 0
    curr_sum = 0

    for i in range(len(nums)):
        curr_sum += nums[i]

        # if curr_sum == k:
        #     count += 1

        #NOTE:   we are not using elif bcos, ex: [1, -1, 0] if we ll use elif  
        # our op ll be 2 but the correct ans is 3

        if curr_sum - k in dic:
            count += dic[curr_sum - k]
        
        dic[curr_sum] += 1

    return count

