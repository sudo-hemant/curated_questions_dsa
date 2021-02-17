

# NOTE:     using morris traversal algo. its quite similar to morris traversal of inorder

# Video reference ----  https://www.youtube.com/watch?v=BuI-EULsz0Y

class Solution:

    def preorder_traversal(self, root):
        
        if not root:
            return []

        result = []
        current = root

        while current:
            
            if not current.left:
                result.append(current.val)
                current = current.right

            else:
                predecessor = self.predecessor(current)

                if not predecessor.right:
                    result.append(current.val)
                    predecessor.right = current
                    current = current.left
                
                elif predecessor.right == current:
                    predecessor.right = None
                    current = current.right



    def predecessor(self, root):
        current = root.left

        while current.right and current.right != root:
            current = current.right

        return current
