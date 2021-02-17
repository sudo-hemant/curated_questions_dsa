

# https://practice.geeksforgeeks.org/problems/max-circular-subarray-sum-1587115620/1

# NOTE: we are modifying kadane algo to find max subarray and min subarray 
# TODO: all solutions of leetcode 

def summ(arr):

    if len(arr) == 1:
        return arr[0]

    total_sum = sum(arr)

    max_so_far, max_ending_here = arr[0], arr[0]
    min_so_far, min_ending_here = arr[0], arr[0]

    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)

        min_ending_here = min(arr[i], min_ending_here + arr[i])
        min_so_far = min(min_so_far, min_ending_here)
    
    # if min_so_far == total_sum:
    #     return max_so_far

    # return max(max_so_far, total_sum - min_so_far)

    return max(max_so_far, total_sum - min_so_far) if max_so_far > 0 else max_so_far