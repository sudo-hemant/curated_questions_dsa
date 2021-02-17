

# NOTE: SOLUTION - 1

# The idea is to begin from last element of ar2[] and search it in ar1[].
# If there is a greater element in ar1[], then we move last element of ar1[] to ar2[]. 
# To keep ar1[] and ar2[] sorted, we need to place last element of ar2[] at correct place in ar1[]. 
# We can use Insertion Sort type of insertion for this


# ------------------------------------------------------------------------------------------------------

# NOTE: SOLUTION - 2

# We start comparing elements that are far from each other rather than adjacent. 
# For every pass, we calculate the gap and compare the elements towards the right of the gap. 
# Every pass, the gap reduces to the ceiling value of dividing by 2. 

def next_gap(gap):
    if gap <= 1:
        return 0

    return (gap + 1) // 2


def merge_1(arr_1, arr_2):

    n, m = len(arr_1), len(arr_2)
    gap = n + m
    gap = next_gap(gap)

    while gap:
        
        # comparing elements in 1st array
        i = 0
        while i + gap < n:
            if arr_1[i] > arr_1[i + gap]:
                arr_1[i], arr_1[i + gap] = arr_1[i + gap], arr_1[i]
            i += 1 

        # comparing elements in both array
        j = gap - n if gap > n else 0
        while i < n and j < m:
            if arr_1[i] > arr_2[j]:
                arr_1[i], arr_2[j] = arr_2[j], arr_1[i]
            
            i, j = i + 1, j + 1

        # comparing elements in 2nd array
        if j < m:
            j = 0
            while j + gap < m:
                if arr_2[j] > arr_2[j + gap]:
                    arr_2[j], arr_2[j + gap] = arr_2[j + gap], arr_2[j] 
                j += 1
        
        gap = next_gap(gap)

    return arr_1, arr_2

print(merge_1(
    [5, 6, 7],
    [1, 2, 3, 4, 5, 6, 7, 8]

))


# ----------------------------------------------------------------------

# NOTE: SOLUTION - 3

# storing 2 values at same location method 

def merge_2(arr_1, arr_2):
    n, m = len(arr_1), len(arr_2)

    maximum = max(arr_1[-1], arr_2[-1]) + 1

    i = j = k = 0

    while i < n and j < m:
        
        e1 = arr_1[i] % maximum
        e2 = arr_2[j] % maximum

        if e1 <= e2:
            if k < n:
                arr_1[k] += (e1 * maximum)
            else:
                arr_2[k - n] += (e1 * maximum)
            
            i = i + 1

        else:
            if k < n:
                arr_1[k] += (e2 * maximum)
            else:
                arr_2[k - n] += (e2 * maximum)

            j = j + 1

        k += 1

    # process those elements which are left in array 1
    while i < n:
        el = arr_1[i] % maximum

        if k < n:
            arr_1[k] += (el * maximum)
        else:
            arr_2[k - n] += (el * maximum)
        
        i, k = i + 1, k + 1
    
    # process those elements which are left in array 2
    while j < m:
        el = arr_2[j] % maximum

        if k < n:
            # TODO: DOUBT
            arr_2[k] += (el * maximum)
        else:
            arr_2[k - n] += (el * maximum)

        j, k = j + 1, k + 1

    for i in range(n):
        arr_1[i] = arr_1[i] // maximum
        
    for j in range(m):
        arr_2[j] = arr_2[j] // maximum

    return arr_1, arr_2


merge_2(
    [3, 5, 6, 8, 12],
    [1, 4, 9, 13]

)