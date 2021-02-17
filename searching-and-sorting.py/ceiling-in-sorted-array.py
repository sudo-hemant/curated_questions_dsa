

def ceiling(arr, find):

    low, high = 0, len(arr) - 1
    ceil = float('inf')

    if find <= arr[low]:
        return arr[low]
    elif arr[high] < find:
        return -1

    while low <= high:
        mid = (high - low) // 2 + low

        if arr[mid] == find:
            return arr[mid]
        elif arr[mid] > find:
            ceil = arr[mid]
            high = mid - 1
        else:
            low = mid + 1

    return ceil


print(ceiling( [1, 2, 8, 10, 10, 12, 19], 0 ))
