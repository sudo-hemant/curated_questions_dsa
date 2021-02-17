
# https://www.geeksforgeeks.org/perfect-binary-tree-specific-level-order-traversal/

# NOTE: 

# Approach 1:

# We can do standard level order traversal here too but instead of printing nodes directly, 
# we have to store nodes in current level in a temporary array or list 1st and then take nodes
# from alternate ends (left and right) and print nodes. Keep repeating this for all levels.
# This approach takes more memory than standard traversal.

# Approach 2:

# The standard level order traversal idea will slightly change here. Instead of processing
# ONE node at a time, we will process TWO nodes at a time. And while pushing children into queue, 
# the enqueue order will be: 1st node’s left child, 2nd node’s right child, 1st node’s right child 
# and 2nd node’s left child.


from collections import deque

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def print_specific_level_order(root):
    if not root:
        return

    print(root.data)

    if root.left:
        print(root.left.data)
        print(root.right.data)

    q = deque()
    q.append(root.left)
    q.append(root.right)

    first = second = None

    while q:
        first = q.popleft()
        second = q.popleft()

        print(first.left.data)
        print(second.right.data)
        print(first.right.data)
        print(second.left.data)

        if first.left.left:
            q.append(first.left)
            q.append(second.right)
            q.append(first.right)
            q.append(second.left)



root = Node(1) 
   
root.left= Node(2) 
root.right   = Node(3) 
   
root.left.left  = Node(4) 
root.left.right = Node(5) 
root.right.left  = Node(6) 
root.right.right = Node(7) 
   
root.left.left.left  = Node(8) 
root.left.left.right  = Node(9) 
root.left.right.left  = Node(10) 
root.left.right.right  = Node(11) 
root.right.left.left  = Node(12) 
root.right.left.right  = Node(13) 
root.right.right.left  = Node(14) 
root.right.right.right  = Node(15) 
   
root.left.left.left.left  = Node(16) 
root.left.left.left.right  = Node(17) 
root.left.left.right.left  = Node(18) 
root.left.left.right.right  = Node(19) 
root.left.right.left.left  = Node(20) 
root.left.right.left.right  = Node(21) 
root.left.right.right.left  = Node(22) 
root.left.right.right.right  = Node(23) 
root.right.left.left.left  = Node(24) 
root.right.left.left.right  = Node(25) 
root.right.left.right.left  = Node(26) 
root.right.left.right.right  = Node(27) 
root.right.right.left.left  = Node(28) 
root.right.right.left.right  = Node(29) 
root.right.right.right.left  = Node(30) 
root.right.right.right.right  = Node(31) 
   
print("Specific Level Order traversal of binary tree is")
print_specific_level_order(root)

