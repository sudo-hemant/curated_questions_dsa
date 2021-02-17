import heapq


# NOTE: we are using concept of merging k sorted arrays


def sorted_print(matrix):

    heap = []
    ans = []

    rows, columns = len(matrix), len(matrix[0])

    for i in range(len(matrix)):
        # stores -- element, row, column
        heap.append((matrix[i][0], i, 0))

    heapq.heapify(heap)

    while heap:
        extract_min, curr_row, curr_col = heapq.heappop(heap)

        ans.append(extract_min)

        if curr_col < columns - 1:
            heap.append((matrix[curr_row][curr_col + 1], curr_row, curr_col + 1))
            heapq.heapify(heap)

    print(*ans)



print(sorted_print(
    [
        [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50]
    ]
))


