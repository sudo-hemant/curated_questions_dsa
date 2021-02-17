
# https://practice.geeksforgeeks.org/problems/maximum-sum-increasing-subsequence4749/1

def maxSumIS(self, arr, n):
	
	if not len(arr):
	    return 0
	elif len(arr) == 1:
	    return arr[0]
	
	lis = [0] * len(arr)
	result = arr[0]
	
	for i, num in enumerate(arr):
	    lis[i] = num
	    
	for i in range(1, len(arr)):
	    for j in range(i):
	        if arr[j] < arr[i]:
	            lis[i] = max(lis[i], lis[j] + arr[i])
	    result = max(result, lis[i])
	    
	return result
