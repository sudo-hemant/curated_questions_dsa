

def countSquares(N):
    
    low, high = 1, N
    ans = 0
    
    while low <= high:
        # this ll prevent integer overflow
        mid = low + (high - low) // 2
        square = mid * mid
        
        if square == N:
            ans = mid - 1
            break
        elif square < N:
            ans = mid 
            low = mid + 1
        elif square > N:
            high = mid - 1
    
    return ans


print(countSquares(9))