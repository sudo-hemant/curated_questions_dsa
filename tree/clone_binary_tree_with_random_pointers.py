
# the problem is if we create direct clone, we ll encounter problem when creating random pointer for the clone, 
# since we won't know that to which node it's random pointer is pointing

# SOLUTION -- we ll create a map, in which we ll store the mapping of the node to its newly created clone   

# TODO:     NOT CHECKED THE CORRECTNESS OF THE PROGRAM

def clone_tree(root):
    if not root:
        return None

    address_map = {}
    
    # first create the cloned tree
    cloned_tree = copy_nodes( root, address_map )

    # copy the random pointers
    copy_random_pointers( root, cloned_tree, address_map )
    
    return cloned_tree


def copy_nodes(root, address_map):
    if not root:
        return None
    
    new_node = Node(root.data)

    # most important part of the algo
    address_map[root] = new_node
    
    new_node.left = copy_nodes(root.left, address_map)
    new_node.right = copy_nodes(root.right, address_map)

    return new_node


def copy_random_pointers(root, cloned_tree, address_map):
    
    if not cloned_tree:
        return 

    # fetch the node to which the current's node random pointer is pointing and
    #  assign the clone of that(destination) node to random pointer of curr node in cloned trees 
    cloned_tree.random = address_map[root.random]

    copy_random_pointers(root.left, cloned_tree.left, address_map)
    copy_random_pointers(root.right, cloned_tree.right, address_map)



#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.random=None

    def __str__(self):
        return str(self.data)

def printInord(a,b):
    if (not a and not b):
        return 1
        
    if(a and b) :
        t=(int)((a.data==b.data) and printInord(a.left,b.left) and printInord(a.right,b.right))
        
        if(a.random and b.random) :
            return (t and a.random.data==b.random.data)
            
        if (a.random==b.random) :
            return t
            
        return 0
    #if a.random.data==b.random.data and printInord(a.left,b.left) and printInord(a.right,b.right):
        #return 1
    return 0


if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        map=dict()

        # n=int(input())
        n = 6
        # arrnode=[x for x in input().split()]
        arrnode = [6, 3, 'L', 6, 8, 'R', 3, 1, 'L', 3, 5, 'R', 1, 3, 'X', 5, 6, 'X']

        root=None
        i=0
        while i<3*n:

            n1,n2,lr=int(arrnode[i]),int(arrnode[i+1]),arrnode[i+2]

            if n1 in map:
                parent=map[n1]
            else:
                parent = Node(n1)
                child=Node(n2)
            map[n2]=child

            if lr=='R':
                parent.right=child

            elif lr=='L':
                parent.left=child

            else:
                parent.random=map[n2]


            i+=3

        ansTree=clone_tree(root)

        print(ansTree)

        if ansTree==root:
            print(0)
        else:
            print(printInord(root,ansTree))

            map[n1] = parent

            if not root:
                root = parent

