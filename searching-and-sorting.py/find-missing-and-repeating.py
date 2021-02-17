

def findTwoElement(arr): 
    ans = []
    
    for i in range(len(arr)):
        if arr[abs(arr[i]) - 1] < 0:
            ans.append(abs(arr[i]))
        else:
            arr[abs(arr[i]) - 1] *= -1
    
    for i in range(len(arr)):
        if arr[i] > 0:
            ans.append(i + 1)
            
    return ans
        
print(findTwoElement([1, 3, 3]))