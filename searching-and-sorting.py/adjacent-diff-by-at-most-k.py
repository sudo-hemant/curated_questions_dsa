

def search(arr, x, k):

    i = 0

    while i < len(arr):
        if arr[i] == x:
            return i
        else:
            diff = abs(arr[i] - x)
            i += max(1, diff // k)

    return -1