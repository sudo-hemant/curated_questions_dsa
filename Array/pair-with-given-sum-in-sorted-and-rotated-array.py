

# NOTE: 

def find_sum(arr, x):

    n = len(arr)

    # finding the pivot element 
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            break

    l = (i + 1) % n
    r = i

    # using same method as finding pair with given sum in sorted array
    # we just need to make sure that we are not moving out of the array,
    # bcos here the array is rotated as well
    while l != r:
        curr_sum = arr[l] + arr[r]

        if curr_sum == x:
            return True
        elif curr_sum < x:
            l = (l + 1) % n
        elif curr_sum > x:
            r = (n + r - 1) % n
    
    return False


print(find_sum(
    [11, 15, 26, 38, 9, 10], 45
))