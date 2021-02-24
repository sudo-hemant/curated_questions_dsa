
# https://leetcode.com/problems/course-schedule-ii/


from typing import List
from collections import defaultdict
class Solution:
    
    # for marking non-visited 
    WHITE = 1
    # for marking currently being visited (its child is being explored)
    GRAY = 2
    # all child visited
    BLACK = 3
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_graph = defaultdict(list)
        
        for dest, src in prerequisites:
            adj_graph[src].append(dest)
        
        # we are using stack, bcos any node might have mutliple parents 
        # so all parents should come before
        topological_sorted_order = []
        is_possible = True

        # marking current status of the node
        color = {k: Solution.WHITE for k in range(numCourses)}
        
        def dfs(node):
            nonlocal is_possible
            
            if not is_possible:
                return 
            
            # mark current node as being visited, and childrens in process
            color[node] = Solution.GRAY
            
            # if child exists
            if node in adj_graph:
                # iterate all childs, and if any child not visited yet, perform dfs
                for neighbour in adj_graph[node]:
                    if color[neighbour] == Solution.WHITE:
                        dfs(neighbour)

                    # NOTE: 
                    # if any child is already gray, that means cycle exists in the graph
                    elif color[neighbour] == Solution.GRAY:
                        is_possible = False
            
            color[node] = Solution.Black
            
            # store it in the stack
            topological_sorted_order.append(node)
            
        for vertex in range(numCourses):
            if color[vertex] == Solution.WHITE:
                dfs(vertex)
                
        return topological_sorted_order[::-1] if is_possible else []
        


# -----------------------------------------------------------------------------------


# NOTE:  METHOD - 2

from collections import defaultdict, deque
class Solution:
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_graph = defaultdict(list)
        indegree = {}
        
        for dest, src in prerequisites:
            adj_graph[src].append(dest)
            
            indegree[dest] = indegree.get(dest, 0) + 1
            
        topological_sorted_order = []
        zero_indegree_queue = deque([k for k in range(numCourses) if k not in indegree])
        
        while zero_indegree_queue:
            
            vertex = zero_indegree_queue.popleft()
            topological_sorted_order.append(vertex)
            
            if vertex in adj_graph:
                for neighbour in adj_graph[vertex]:
                    indegree[neighbour] -= 1
                    
                    if indegree[neighbour] == 0:
                        zero_indegree_queue.append(neighbour)
                        
        return topological_sorted_order if len(topological_sorted_order) == numCourses else []