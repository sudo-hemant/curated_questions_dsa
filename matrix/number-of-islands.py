from collections import deque


def num_islands(grid):
    count = 0
    is_visited = [ [False] * len(grid[0]) for _ in range(len(grid)) ]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1' and not is_visited[i][j]:
                expand_island(i, j, is_visited, len(grid), len(grid[0]), grid)
                count += 1

    return count 


def expand_island(i, j, is_visited, rows, cols, grid):
    row = [0, -1, 0, 1]
    col = [-1, 0, 1, 0]
    q = deque()

    q.append((i, j))
    is_visited[i][j] = True

    while q:
        x, y = q.popleft()

        for add in range(4):
            if is_safe(x + row[add], y + col[add], rows, cols, is_visited) and grid[x + row[add]][y + col[add]] == '1':
                q.append((x + row[add], y + col[add]))
                is_visited[x + row[add]][y + col[add]] = True


def is_safe(i, j, rows, cols, is_visited):
    if 0 <= i < rows and 0 <= j < cols and not is_visited[i][j]:
        return True
    return False




print(num_islands(
    [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
    ]
))