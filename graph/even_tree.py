
# https://www.hackerrank.com/challenges/even-tree/problem


# NOTE: we do dfs and return the child nodes, if there is any child with even nodes
# we cut the link of that child node from its parent


import math
import os
import random
import re
import sys
from collections import defaultdict

def dfs(vertex, is_visited, graph):
    is_visited[vertex] = True
    childs = 0
    
    for neighbour in graph[vertex]:
        if not is_visited[neighbour]:

            grand_childs = dfs(neighbour, is_visited, graph)
            
            # if any subtree has even nodes, we break that link
            if grand_childs % 2 == 0:
                evenForest.edges_removed += 1
            # else:
            #     childs += grand_childs

            # NOTE:  OR
            childs += grand_childs
                
    return childs + 1


def evenForest(nodes, graph):
    is_visited = [False] * (nodes + 1)

    # to store the removed nodes
    evenForest.edges_removed = 0

    # because the graph will be connected
    dfs(1, is_visited, graph)
    
    return evenForest.edges_removed    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())
    graph = defaultdict(list)

    for i in range(t_edges):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    res = evenForest(t_nodes, graph)
    fptr.write(str(res) + '\n')
    fptr.close()
    