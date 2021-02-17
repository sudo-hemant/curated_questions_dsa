
# NOTE:     using two stacks

# The idea is to push reverse postorder traversal to a stack,
# Now the question is, how to get reversed postorder elements in 
# a stack – the second stack is used for this purpose. For example,
#  in the following tree, we need to get 1, 3, 7, 6, 2, 5, 4 in a stack. 
# If take a closer look at this sequence, we can observe that this sequence 
# is very similar to the preorder traversal. The only difference is that the 
# right child is visited before left child, and therefore the sequence is “root right left”
#  instead of “root left right”. So, we can do something like iterative preorder traversal with the following differences:
# a) Instead of printing an item, we push it to a stack.
# b) We push the left subtree before the right subtree.

# https://www.geeksforgeeks.org/iterative-postorder-traversal/

class Solution:
    def postOrderTraversal(self, root):
        
        if not root:
            return []

        result = []
        stack = []

        stack.append(root)

        while stack:
            popped = stack.pop()
            result.append(popped.val)
    
            if popped.left:
                stack.append(popped.left)
            if popped.right:
                stack.append(popped.right)

        left, right = 0, len(result) - 1

        while left < right:
            result[left], result[right] = result[right], result[left]
            left, right = left + 1, right - 1

        return result
            

# ----------------------------------------------------------------------------


# NOTE: using only one stack

class Solution2:
    def post_order_traversal(self, root):

        if not root:
            return []

        stack = []
        result = []

        current = root

        while True:

            while current:
                if current.right:
                    stack.append(current.right)
                stack.append(current)
                current = current.left

            current = stack.pop()
            
            if current.right and stack and current.right == stack[-1]:
                stack.pop()
                stack.append(current)
                current = current.right
            
            else:
                result.append(current.val)
                current = None
                
            if not stack:
                break
                
        return result