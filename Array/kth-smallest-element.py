
# NOTE: it is min heap, every time we pop element, it pops minimum element 
# and we need smallest element, so we are going to push element by changing its sign 

import heapq

def kthSmallest(arr, l, r, k):
    '''
    arr : given array
    l : starting index of the array i.e 0
    r : ending index of the array i.e size-1
    k : find kth smallest element and return using this function
    '''
    
    heap = []
    
    for num in arr:
        if len(heap) < k:
            heapq.heappush(heap, -1 * num)
        else:
            curr_min = -1 * heapq.heappop(heap)
            heapq.heappush(heap, -1 * min(curr_min, num))
            
    return -1 * heapq.heappop(heap)
