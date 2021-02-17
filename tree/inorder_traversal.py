
# https://leetcode.com/problems/binary-tree-inorder-traversal/


# NOTE:    using stack

class Solution:
    def inorderTraversal(self, root):
        
        if not root:
            return []
        
        stack = []
        result = []
        
        stack.append(root)
        current = root.left
        
        while True:
            
            while current:
                stack.append(current)
                current = current.left

            if stack:
                popped_element = stack.pop()
                
                result.append(popped_element.val)
                current = popped_element.right
            
            else:
                break

        return result



# NOTE:     using morris traversal
# Video reference ----  https://www.youtube.com/watch?v=BuI-EULsz0Y


class Solution2:
    def inorderTraversal2(self, root):

        if not root:
            return []

        result = []
        current = root

        while current:
            if not current.left:
                result.append(current.val)
                current = current.right

            else:
                # finds right most node in left subtree
                predecessor = self.predecessor(current)

                # if the link is not created to its predecessor, then we ll create it i.e., predecessor.right = current
                if not predecessor.right:
                    predecessor.right = current
                    current = current.left

                # if the link already exists, then we delete the link ( which was created by us)
                elif predecessor.right == current:
                    predecessor.right = None
                    result.append(current.val)
                    current = current.right                                    
        
        return result

    def predecessor(self, root):
        current = root.left

        while current.right and current.right != root:
            current = current.right

        return current