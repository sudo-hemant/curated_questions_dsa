
# https://www.geeksforgeeks.org/diagonal-traversal-of-binary-tree/

# NOTE:     this problem is quite similar to vertical traversal of binary tree,
#           here we keep track of a the current level, and assign +1 to its left child
#           and same level to right child and store it in dictionary i.e., default dict
#           to save accessing dictionary twice for same operations


from collections import defaultdict

def diagonal(root):

    dic = defaultdict(list)
    ans = []
    deepest = [0]
    
    diagonal_util(root, 0, dic, deepest)
    
    # for i in range(0, diagonal_util.deepest + 1):
    #     ans.extend(dic[i])
    
    for i in range(0, deepest[0] + 1):
        ans.extend(dic[i])
    
    return ans
    
    
def diagonal_util(root, level, dic, deepest):
    if not root:
        return 
    
    dic[level].append(root.data)

    diagonal_util(root.left, level + 1, dic, deepest)
    diagonal_util(root.right, level, dic, deepest)
    
    deepest[0] = max(deepest[0], level)
    # diagonal_util.deepest = max(diagonal_util.deepest, level)
