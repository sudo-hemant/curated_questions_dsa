

# NOTE: same as dutch national flag
# if the curr is less than a send it to left side,
# if greater than b send it to right side,
# if between a and b leave it as it is, and check for next element

def threeWayPartition(self, arr, a, b):
    
    low, curr, high = 0, 0, len(arr) - 1
    
    while curr <= high:

        # NOTE: this commented part is just for saving some time ( make our sol little faster )

        # while low < high and arr[low] < a:
        #     low += 1
        # while low < high and arr[high] > b:
        #     high -= 1
        
        # if curr < low:
        #     curr = low 
        
        
        if arr[curr] < a:
            arr[low], arr[curr] = arr[curr], arr[low]
            low, curr = low + 1, curr + 1
        
        elif arr[curr] > b:
            arr[curr], arr[high] = arr[high], arr[curr]
            high -= 1
    
        else:
            curr += 1