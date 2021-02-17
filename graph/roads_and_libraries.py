
# https://www.hackerrank.com/challenges/torque-and-development/problem?isFullScreen=false

# NOTE: tried greedy approach

import math
import os
import random
import re
import sys
from collections import defaultdict

# return count of the nodes that can be visited from the current node.
def dfs(vertex, is_visited, cities, count):
    is_visited.add(vertex)
    count += 1
    
    for neighbour in cities[vertex]:
        if neighbour not in is_visited:
            count = dfs(neighbour, is_visited, cities, count)
    
    return count
    
    
def roadsAndLibraries(n, c_lib, c_road, cities):
    total_cost = 0
    is_visited = set()
    
    for vertex in range(1, n + 1):
        if vertex not in is_visited:
            connected_nodes = dfs(vertex, is_visited, cities, 0)
            
            # we ll always need atleast one library, and if the cost of library is less, we ll 
            # build library in every city else we ll build road, thats why we have taken min(function)
            # and multiplied it wid the possibility of remaining roads
            total_cost += c_lib + min(c_lib, c_road) * (connected_nodes - 1)
            
    return total_cost
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        # adjacency list graph
        cities = defaultdict(list)

        for _ in range(m):
            u, v = list(map(int, input().rstrip().split()))

            # bcos 2 way road is possible
            cities[u].append(v)
            cities[v].append(u)

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
