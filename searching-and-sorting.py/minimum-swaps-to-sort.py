
# NOTE: this is kind of maths 


def minSwaps(arr, N):
    
    sorted_arr = [] * N
    ans = 0
    
    for (i, num) in enumerate(arr, 0):
        sorted_arr.append([num, i])
    
    sorted_arr.sort()
    is_visited = [False] * N
    
    for i in range(N):
        if is_visited[i] or sorted_arr[i][1] == i:
            continue
        
        j = i
        cycle_size = 0
        
        while not is_visited[j]:
            is_visited[j] = True
            cycle_size += 1
            j = sorted_arr[j][1]
        
        ans += cycle_size - 1
    
    return ans
