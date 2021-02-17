
# https://practice.geeksforgeeks.org/problems/equilibrium-point-1587115620/1

def equilibriumPoint(arr, N):

    if not len(arr):
        return -1
    if len(arr) == 1:
        return 1
        
    forward_sum, backward_sum = [0] * len(arr), [0] * len(arr)
    forward_sum[0], backward_sum[-1] = arr[0], arr[-1] 
    
    for i in range(1, len(arr)):
        forward_sum[i] = forward_sum[i - 1] + arr[i]
    
    for i in reversed(range(len(arr) - 1)):
        backward_sum[i] = backward_sum[i + 1] + arr[i]

    for i in range(len(arr)):
        if forward_sum[i] == backward_sum[i]:
            return i + 1
    
    return -1




# 2nd method - better than the above 
def equilibrium(arr): 
  
    # finding the sum of whole array 
    total_sum = sum(arr) 
    leftsum = 0
    for i, num in enumerate(arr): 
          
        # total_sum is now right sum 
        # for index i 
        total_sum -= num 
          
        if leftsum == total_sum: 
            return i 
        leftsum += num 
       
      # If no equilibrium index found,  
      # then return -1 
    return -1