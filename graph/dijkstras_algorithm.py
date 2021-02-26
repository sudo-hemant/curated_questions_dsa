
# TODO:     WRITE AND UNDERSTAND TIME COMPLEXITY PROPERLY

# NOTE:     this problem is quite similar to BFS, but instead of using queue, we are using priority queue
    # best reference -- pepcoding 

# NOTE:     We can also use heap to find the minimum weighted edge insted of using the function min_weight_in_non_spt
#            to reduce time complexity

class Solution:

    def dijkstra(self, V, adj, S):
        
        # to store the minimum distances of every node from the source node
        min_dist_from_source = [float('inf')] * V

        # distance of source node from source node is 0
        min_dist_from_source[S] = 0

        # to indicate whether the particular node is already processed or not
        spt_set = [False] * V
        
        for _ in range(V):
            # find the minimum weight edge among all edges which is not processed yet
            min_index = self.min_weight_in_non_spt(min_dist_from_source, spt_set, V)

            # mark the current node as visited/processed/included in spt(spanning tree)
            spt_set[min_index] = True

            # visits all adjacents of the current node and update the distance of the unprocessed node
            for adjacents, cost in adj[min_index]:
                if not spt_set[adjacents] and min_dist_from_source[adjacents] > min_dist_from_source[min_index] + cost:
                    min_dist_from_source[adjacents] = min_dist_from_source[min_index] + cost

        return min_dist_from_source


    # finds the minimum weight node, among all the nodes which are not processed yet
    def min_weight_in_non_spt(self, min_dist_from_source, spt_set, V):
        minimum_weight, minimum_index = float('inf'), -1
        
        for v in range(V):
            if min_dist_from_source[v] < minimum_weight and not spt_set[v]:
                minimum_weight = min_dist_from_source[v]
                minimum_index = v

        return minimum_index



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
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()