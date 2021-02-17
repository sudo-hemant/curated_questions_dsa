

# NOTE: O(N ^ 2) solution

# we consider every index as starting index and calculate the ans
# and return the max sum
def max_sum(a,n):
    
    ans = float('-inf')
    
    for i in range(n):
        curr_sum = 0
        
        for j in range(n):
            index = (i + j) % n
            curr_sum += a[index] * j
            
        ans = max(ans, curr_sum)
        
    return ans


# ------------------------------------------------------------

# NOTE: O(N) solution

# the trick here is we can calulate the curr value from prev value, 
# since the first element which was contributing 0 to the prev value
# ll mutlipled by max no in the curr value
# ex : arr = 1, 2, 3
# 1 * 0 + 2 * 1 + 3 * 2 = 8
# now for the next iteration our array ll become 
# 2 * 0 + 3 * 1 + 1 * 2 = 5

# here we can see that the first element which was contributing 0 in prev value, 
# has been mutliplied by max (i) in curr val
# so curr_sum = prev_sum + arr[i - 1](first element of prev iteration) * (len(arr) - 1)

# now since for every no the multiplier has been reduced by 1, 
# so the value which we ll need to subtract is 
# 2 * 1 + 3 * 1 = 2 + 3
# and we hv already found out the sum of the all terms, but we need to take care that 
# the first element of prev iteration was contributing 0 so we ll subtract 
# total_sum_of_array - first element of prev array

# hence our formula becomes 
# curr_sum = prev_sum + arr[i - 1] * (n - 1) - (total_arr_sum - arr[i - 1])

def max_sum_2(arr, n):
    ans = float('-inf')
    
    arr_sum = sum(arr)
    
    prev_sum = 0
    for i, num in enumerate(arr):
        prev_sum += num * i
    
    ans = max(ans, prev_sum)
    
    for i in range(1, n):
        prev_sum = prev_sum + arr[i - 1] * (n - 1) - (arr_sum - arr[i - 1])
        ans = max(ans, prev_sum)

    return ans

