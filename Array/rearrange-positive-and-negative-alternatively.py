

# NOTE: TC : O(N) and sc : O(1)

# here we first separate negative and positive elements like quick sort pivot method
# then arrange them alternately, by keeping 2 index, one at starting of negative elements
# second at starting of positive elements
def rearrange(self,arr, n):

    i = -1 
    for j in range(n):
        if arr[j] < 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    negative, positive = 0, i + 1
    
    while positive < n and negative < positive and arr[negative] < 0:
        arr[negative], arr[positive] = arr[positive], arr[negative]
        negative, positive = negative + 2, positive + 1
