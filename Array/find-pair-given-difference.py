
tests = int(input())
for _ in range(tests):
    
    size, diff = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    i, j = 0, 1
    flag = False
    
    arr.sort()
    
    while i <= j and j < len(arr):
        if i == j:
            j += 1
        elif i != j and arr[j] - arr[i] == diff:
            flag = True
            break
        elif arr[j] - arr[i] < diff:
            j += 1
        else:
            i += 1
            
    if flag:
        print(1)
    else:
        print(-1)
    