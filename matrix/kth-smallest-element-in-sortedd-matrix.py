import heapq


def kth_smallest(matrix, k):

    heap = []
    smallest_popped = 0
    ans = 0

    for i in range(len(matrix)):
        heap.append((matrix[i][0], i, 0))

    heapq.heapify(heap)

    while smallest_popped < k:
        popped, i, j = heapq.heappop(heap)
        smallest_popped += 1
        ans = popped

        if j < len(matrix[0]) - 1:
            heap.append((matrix[i][j + 1], i, j + 1))
            heapq.heapify(heap)

    return ans


print( kth_smallest( 
    [
        [ 1,  5,  9],
        [10, 11, 13],
        [12, 13, 15]
    ], 
    8
 ) )


