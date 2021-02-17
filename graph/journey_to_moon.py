
# https://www.hackerrank.com/challenges/journey-to-the-moon/problem?isFullScreen=true

# NOTE: similar to roads & libraries problme, we count astronauts by country and store
# them in the list and then calulate the total ways 


import math
import os
import random
import re
import sys
from collections import defaultdict

def dfs(vertex, is_visited, astronaut, count):
    is_visited[vertex] = True
    count += 1

    for neighbour in astronaut[vertex]:
        if not is_visited[neighbour]:
            count = dfs(neighbour, is_visited, astronaut, count)
            
    return count
    

def journeyToMoon(n, astronaut):
    # store astronauts count by their countries
    astronaut_count_by_countries = []

    is_visited = [False] * n

    # to help us calculate the ways we can group astronauts 
    postfix_sum = n
    total_ways = 0
    
    for vertex in range(n): 

        # if the astronaut is alone which is not included in adjacency list
        if not astronaut[vertex] and not is_visited[vertex]:
            astronaut_count_by_countries.append(1)
        elif not is_visited[vertex]:
            same_country_count = dfs(vertex, is_visited, astronaut, 0)
            astronaut_count_by_countries.append(same_country_count)
    
    # method to calculate the total no of ways
    for i in range(len(astronaut_count_by_countries) - 1):
        postfix_sum -= astronaut_count_by_countries[i]
        total_ways += astronaut_count_by_countries[i] * postfix_sum
        
    return total_ways
            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n, p = list(map(int, input().split()))
    astronaut = defaultdict(list)

    for _ in range(p):
        a, b = list(map(int, input().split()))
        astronaut[a].append(b)
        astronaut[b].append(a)
        
    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')
    fptr.close()
