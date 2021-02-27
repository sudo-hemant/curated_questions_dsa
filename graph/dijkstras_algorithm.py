

# NOTE:     this problem is quite similar to BFS, but instead of using queue, we are using priority queue
    # best reference -- pepcoding 

# NOTE:     We can also use heap to find the minimum weighted edge insted of using the function min_weight_in_non_spt
#            to reduce time complexity


# NOTE:

# The code calculates shortest distance, but doesn’t calculate the path information. We can create
# a parent array, update the parent array when distance is updated (like prim’s implementation) 
# and use it show the shortest path from source to different vertices.

# The code is for undirected graph, same dijkstra function can be used for directed graphs also.

# The code finds shortest distances from source to all vertices. If we are interested only in shor
# test distance from source to a single target, we can break the for loop when the picked minimum
# distance vertex is equal to target (Step 3.a of algorithm).

# Dijkstra’s algorithm doesn’t work for graphs with negative weight edges. For graphs with negativ
# e weight edges, Bellman–Ford algorithm can be used, we will soon be discussing it as a separate post.


class Solution:

    def dijkstra(self, V, adj, S):
        
        # to store the minimum distances of every node from the source node
        min_dist_from_source = [float('inf')] * V

        # distance of source node from source node is 0
        min_dist_from_source[S] = 0

        # to indicate whether the particular node is already processed or not
        spt_set = [False] * V
        
        # Tc  --  O(V)
        for _ in range(V):

            # Tc  ---  O(V) 
            # if min-heap is used, it can be reduced to O(log(V)) and overall will be O(V log(v))
            # find the minimum weight edge among all edges which is not processed yet
            min_index = self.min_weight_in_non_spt(min_dist_from_source, spt_set, V)

            # mark the current node as visited/processed/included in spt(spanning tree)
            spt_set[min_index] = True

            # since here it is adjacency list  --  O(V + E) overall 
            # NOTE: don't multiply this tc with the outer loop bcos O(V + E) is tc after considering
            # outer loop as well

            # visits all adjacents of the current node and update the distance of the unprocessed node
            for adjacents, cost in adj[min_index]:
                if not spt_set[adjacents] and min_dist_from_source[adjacents] > min_dist_from_source[min_index] + cost:
                    
                    # Tc -- this takes log(v) time
                    min_dist_from_source[adjacents] = min_dist_from_source[min_index] + cost

        return min_dist_from_source

    # NOTE: Tc  --  O(V)
    # finds the minimum weight node, among all the nodes which are not processed yet
    def min_weight_in_non_spt(self, min_dist_from_source, spt_set, V):
        minimum_weight, minimum_index = float('inf'), -1
        
        for v in range(V):
            if min_dist_from_source[v] < minimum_weight and not spt_set[v]:
                minimum_weight = min_dist_from_source[v]
                minimum_index = v

        return minimum_index


    # NOTE: Tc is O(V^2) and if adjacency list and min heap is used it will be O(V log(v)) + O((V + E) log(v))


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