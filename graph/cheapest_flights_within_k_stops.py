

# NOTE:     a little variant of dikstra's algo


# https://leetcode.com/problems/cheapest-flights-within-k-stops/


from typing import List
from collections import defaultdict, deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        adj_graph = defaultdict(list)

        # to store the minimum cost to reach the current node
        cost_to_reach = defaultdict(lambda : float('inf'))
        queue = deque()

        for u, v, cost in flights:
            adj_graph[u].append((v, cost))

        # to store the node, cost, the current stop nubmer
        queue.append((src, 0, -1))

        while queue:
            city, cost, k = queue.popleft()

            # if we have already reached the destination or crossed the maximum stop limit
            if city == dst or k == K:
                continue
            
            for neighbour, price in adj_graph[city]:

                # if the node is already visited and its current cost is greater than the 
                # minimum cost by which we can reach the current node
                if cost + price >= cost_to_reach[neighbour]:
                    continue

                # else if the node is unreached till now or the cost is smaller than the
                # previous stored value
                cost_to_reach[neighbour] = cost + price
                queue.append((neighbour, cost + price, k + 1))

        return cost_to_reach[dst] if cost_to_reach[dst] != float('inf') else -1

