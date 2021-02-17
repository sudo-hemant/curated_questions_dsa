
def move(arr):

    i, j = 0, len(arr) - 1

    while i < j:
        if arr[i] < 0:
            i += 1
        elif arr[i] >= 0:
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1
    return arr


print(move([ 1, 2, 5, 5, 3, 0, -1, -3, -4, -5, 0, 8, -10 ]))