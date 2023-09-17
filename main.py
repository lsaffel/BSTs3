# started with the code from 34-BSTs

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def insertIntoBST(root_ptr: TreeNode, val: int) -> TreeNode:
#     new_node = TreeNode(val)
#     if root_ptr is None:
#         root = new_node
#         return root
#
#     if val < root_ptr.val:
#         root_ptr = insertIntoBST(root_ptr.left, val)
#     else:       # val >= root.val
#         root_ptr = insertIntoBST(root_ptr.right, val)
#
#     return root_ptr
# ---------------------------------------------------------------
def insertIntoBST(node, val):
    # return a new node if the tree is empty
    if node is None:
        return TreeNode(val)

    if val < node.val:
        node.left = insertIntoBST(node.left, val)
    else:
        node.right = insertIntoBST(node.right, val)

    return node

def levelOrder(root_ptr):
    # prints the nodes of the tree in breadth-first order, i.e. each level
    print("Doing a level order traversal of the tree, starting now ----------")
    q = []      # an empty queue, represented by a list
    # print("The root node's value is: ", root.val)
    valuesList = []         # initialize the list that holds the tree's nodes, traversed breadth first

    q.append(root_ptr)

    while q:        # while q is not empty
        current_node = q.pop(0)

        # add that node's value to the list
        valuesList.append(current_node.val)

        # check the node's children. If they are not null, add them to the queue
        if current_node.left is not None:
            q.append(current_node.left)
        if current_node.right is not None:
            q.append(current_node.right)

    print("The list of node values is now: ", valuesList)

    # -------------------------------------------------------------------


if __name__ == '__main__':
    myTree = TreeNode(17)
    # print(myTree.val)
    levelOrder(myTree)     # prints the nodes of the tree in breadth-first order, i.e. each level
    myTree = insertIntoBST(myTree, 25)
    print(myTree.right.val)

    levelOrder(myTree)     # prints the nodes of the tree in breadth-first order, i.e. each level

    myTree = insertIntoBST(myTree, 12)
    levelOrder(myTree)     # prints the nodes of the tree in breadth-first order, i.e. each level

    print("The root node is: ", myTree.val)
    print("The left node is: ", myTree.left.val)
    print("The right node is: ", myTree.right.val)

    thirdTree = insertIntoBST(myTree, 6)

    levelOrder(myTree)     # prints the nodes of the tree in breadth-first order, i.e. each level
    #
    myTree = insertIntoBST(myTree, 14)
    levelOrder(myTree)     # prints the nodes of the tree in breadth-first order, i.e. each level

    myTree = insertIntoBST(myTree, 15)
    levelOrder(myTree)     # prints the nodes of the tree in breadth-first order, i.e. each level

    myTree = insertIntoBST(myTree, 23)
    levelOrder(myTree)     # prints the nodes of the tree in breadth-first order, i.e. each level
