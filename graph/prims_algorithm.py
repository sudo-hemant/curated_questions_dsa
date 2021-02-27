

# NOTE  this problem is quite similar to dijkstra's algorithm
        # for more clarity check and understand the problem with its
        # time complexity mentioned by me and notes and important points as well


class Solution:
    def prims_algorithm(self, V, adj):
        
        mst = [False] * V
        parent = [None] * V
        distance = [float('inf')] * V
        sum_msp = 0
        
        parent[0] = -1
        distance[0] = 0

        for _ in range(V):
            min_index = self.min_weight(distance, mst, V)
            mst[min_index] = True
            sum_msp += distance[min_index]

            for adjacent, cost in adj[min_index]:
                if not mst[adjacent]:
                    distance[adjacent] = min(distance[adjacent], cost)
                    parent[adjacent] = min_index

        return sum_msp


    def min_weight(self, distance, mst, V):
        min_weight, min_index = float('inf'), -1

        for v in range(V):
            if distance[v] < min_weight and not mst[v]:
                min_weight = distance[v]
                min_index = v
        
        return min_index

        

import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.prims_algorithm(V,adj))