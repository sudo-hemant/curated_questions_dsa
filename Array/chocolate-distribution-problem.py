
tests = int(input())
for _ in range(tests):
    
    size = int(input())
    arr = [int(x) for x in input().split()]
    students = int(input())
    
    i, j = 0, students - 1    
    ans = float('inf')
    arr.sort()
    
    while j < len(arr):
        ans = min(ans, arr[j] - arr[i])
        i, j = i + 1, j + 1
        
    print(ans)


