
# NOTE: THIS PROBLEM IS QUITE SIMILAR TO CHEAPEST FLIGHT WITHIN K STOPS PROBLEM


# https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/monk-and-the-islands/


from collections import defaultdict, deque

tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())

    # adjacency graph of undirected graph
    adj_graph = defaultdict(list)

    # to store the shortest distance from the starting position to the current position
    shortest_distance = defaultdict(lambda : float('inf'))

    # for traversal
    queue = deque()

    for _ in range(m):
        u, v = map(int, input().split())
        adj_graph[u].append(v)
        adj_graph[v].append(u)

    # distance of starting node from itself is 0
    shortest_distance[1] = 0

    # stores the node and the minimum distance to reach it
    queue.append((1, 0))

    while queue:
        island_no, distance = queue.popleft()

        if island_no == n:
            continue

        for neighbour in adj_graph[island_no]:

            # if the neighbour is already processed and the distance to reach it is found to 
            # be smaller or equal to the current distance
            if distance + 1 >= shortest_distance[neighbour]:
                continue

            # else if the current distance is minimum or the node is not processed yet,
            # update the minimum distance to reach the current node
            shortest_distance[neighbour] = distance + 1
            queue.append((neighbour, distance + 1))

    print(shortest_distance[n])