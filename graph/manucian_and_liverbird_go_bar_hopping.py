

# TODO: NOT COMPLETED YET

# NOTE: THIS METHOD WILL GIVE US TLE BCOS WE WILL REVERSE AND TRAVERSE GRAPH AGAIN AND AGAIN TO 
#       FIND THE ANS, SO TO OPTIMIZE WE WILL STORE IT IN ARRAY, LOOK AT METHOD -- 2

from collections import defaultdict
def dfs(node, adj_graph, count):
    
    for neighbour in adj_graph[node]:
        count = dfs(neighbour, adj_graph, count + 1)
    
    return count


def reverse_direction(adj_graph):
    pass


# if __name__ == '__main__':
    
#     size = int(input())
#     directions = [int(x) for x in input().split()]
#     operations = int(input())
#     result = []

#     adj_graph = defaultdict(list)
    
#     for i in range(1, size):
#         if directions[i - 1]:
#             adj_graph[i].append(i + 1)
#         else:
#             adj_graph[i + 1].append(i)



#     for _ in range(operations):
#         update_or_query = list(input().split())
        
#         if update_or_query[0] == 'Q':
#             temp = dfs( int(update_or_query[1]), adj_graph, 0 )
#             result.append(temp + 1)
#         else:
#             reverse_direction(adj_graph)

#     print(result)



# ----------------------------------------------------------------------


# NOTE:     METHOD -- 2


size = int(input())

# to store the directions of the node 
directions = [int(x) for x in input().split()]

# store the ans
result = []

# the first row will store the possible paths from left and the second row will store the 
# paths from left if the direction gets reversed
left_reach = [ [0] * size ] * 2

# the first row will store the possible paths from right and the second row will store the 
# paths from right if the direction gets reversed
right_reach = [ [0] * size ] * 2

# there will be always one way from left for the first node (i.e. from itself)
left_reach[0][0] = 1 
left_reach[1][0] = 1

# there will be always one way from right for the last node (i.e. from itself)
right_reach[0][-1] = 1 
right_reach[1][-1] = 1 

# iterate for the second node till the last, 
# first row will store the paths from left and second row will store the paths from 
# left if the edges gets reversed
for i in range(1, size):
    if directions[i - 1]:
        left_reach[0][i] = left_reach[0][i - 1] + 1
        left_reach[1][i] = 1
    else:
        left_reach[0][i] = 1
        left_reach[1][i] = left_reach[1][i - 1] + 1

# iterate from the last second node till the first, 
# first row will store the paths from right and second row will store the paths from 
# right if the edges gets reversed
for i in reversed(range(size - 1)):
    if directions[i]:
        right_reach[0][i] = 1
        right_reach[1][i] = right_reach[1][i + 1] + 1
    else:
        right_reach[0][i] = right_reach[0][i + 1] + 1
        right_reach[1][i] = 1

# to store the current direct of nodes, 
# if its 0 that means the direction is same as the directions given
# if its 1 that means the direction is opposite of the directions which was given to us 
type = 0
operations = int(input())

for _ in range(operations):
    update_or_query = list(input().split())

    if update_or_query[0] == 'Q':
        s = update_or_query[1]
        total_paths = left_reach[int(s) - 1][type] + right_reach[int(s) - 1][type] - 1

        # total_paths = left_reach[int(s) - 1][type] + right_reach[int(s) - 1][type] - 1
        # result.append(total_paths)
        print(total_paths)
    else:
        type ^= 1

# print(result)