

# https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0

tests = int(input())
for _ in range(tests):
    
    size, k = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    mp = {}
    curr_sum = 0
    flag = False
    
    for i in range(len(arr)):
        curr_sum += arr[i]
        
        if curr_sum == k:
            print(1, i + 1)
            flag = True
            break
        elif curr_sum > k:
            to_find = curr_sum - k
            if to_find in mp:
                print(mp[to_find] + 2, i + 1)
                flag = True
                break
        mp[curr_sum] = i
    
    if not flag:
        print(-1)





# 2nd method - better method, but only handles +ve number
# since all no are +ve, if sum is greater than the target, 
# therefore it ll never happen that by adding any ele we get target 

def subArraySum(arr, n, sum): 
      
    # Initialize curr_sum as 
    # value of first element 
    # and starting point as 0  
    curr_sum = arr[0] 
    start = 0
  
    # Add elements one by  
    # one to curr_sum and  
    # if the curr_sum exceeds  
    # the sum, then remove  
    # starting element  
    i = 1
    while i <= n: 
          
        # If curr_sum exceeds 
        # the sum, then remove 
        # the starting elements 
        while curr_sum > sum and start < i-1: 
          
            curr_sum = curr_sum - arr[start] 
            start += 1
              
        # If curr_sum becomes 
        # equal to sum, then 
        # return true 
        if curr_sum == sum: 
            print ("Sum found between indexes") 
            print ("% d and % d"%(start, i-1)) 
            return 1
  
        # Add this element  
        # to curr_sum 
        if i < n: 
            curr_sum = curr_sum + arr[i] 
        i += 1
  
    # If we reach here,  
    # then no subarray 
    print ("No subarray found") 
    return 0
  