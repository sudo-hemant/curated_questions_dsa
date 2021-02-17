
def rowWithMax1s(arr, n, m):

    ans = 0, -1
    
    for i in range(len(arr)):
        index = first_occurence(arr[i])
        
        if len(arr[0]) - index > ans[0]:
            ans = len(arr[0]) - index, i
    
    return ans[1]
    
    
def first_occurence(arr):
    
    if arr[0] == 1:
        return 0
    elif arr[-1] == 0:
        return len(arr)
        
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] == 1:
            if mid == 0 or arr[mid - 1] == 0:
                return mid
            high = mid - 1
        else:
            low = mid + 1
    



# ----------------------------------------------------


# NOTE:  this can be optimised further 


def max_1s(arr):

    ans = 0, -1
    
    for i in range(len(arr)):

        if ans[1] == -1 or arr[i][len(arr[0]) - ans[0] - 1] == 1:
            index = first_occurence(arr[i])

            # since we want first row with max 1s, otherwise we could have removed this if condition
            if len(arr[0]) - index > ans[0]:
                ans = len(arr[0]) - index, i
    
    return ans[1]
