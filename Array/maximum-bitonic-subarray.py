

# NOTE: tc : O(N) and sc : O(N)

# we are storing forward increasing (like done in LIS) in left arr
# and backward increasing in right arr
# then we sum both left[i] and right[i] at every index
# and returing the max obtained in the whole arr

def bitonic(arr, n):

    left = [1] * n
    right = [1] * n
    ans = 0

    for i in range(1, n):
        if arr[i - 1] <= arr[i]:
            left[i] += left[i - 1]

    for i in reversed(range(n - 1)):
        if arr[i] >= arr[i + 1]:
            right[i] += right[i + 1]

    for i in range(n):
        ans = max(ans, left[i] + right[i] - 1)

    return ans


print(bitonic(
    [12, 4, 78, 90, 45, 23],
    6
))


# -------------------------------------------------------


# NOTE: tc : O(N) and sc : O(1)


def bitonic_modified(arr, n):
    if not len(arr):
        return 0

    curr = 0
    max_len = 1 
    start, next_start = 0, 0

    while curr < len(arr) - 1:
        
        while curr < len(arr) - 1 and arr[curr] <= arr[curr + 1]:
            curr += 1
        
        while curr < len(arr) - 1 and arr[curr] >= arr[curr + 1]:
            if arr[curr] > arr[curr + 1]:
                next_start = curr + 1
            
            curr += 1

        max_len = max(max_len, curr - start + 1)
        start = next_start

    return max_len



print(bitonic_modified(
    [12, 4, 78, 90, 45, 23],
    6
))