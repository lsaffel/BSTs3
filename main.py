# started with the code from 34-BSTs

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertIntoBST(self: TreeNode, val: int) -> TreeNode:
    new_node = TreeNode(val)
    if self is None:
        root = new_node
        return root

    if val < self.val:
        if self.left is None:
            self.left = new_node
        else:
            self.insertIntoBST(self.left, val)
    else:       # val > root.val
        if self.right is None:
            self.right = new_node
        else:
            self.insertIntoBST(self.right, val)

    return self
# ---------------------------------------------------------------


def levelOrder(root):
    # prints the nodes of the tree in breadth-first order, i.e. each level
    print("Doing a level order traversal of the tree, starting now ----------")
    q = []      # an empty queue, represented by a list
    print("The root node's value is: ", root.val)
    valuesList = []         # initialize the list that holds the tree's nodes, traversed breadth first

    q.append(root)
    print("The queue's first element is now: ", q[0].val)

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
    print("The queue is now: ", q)

    # -------------------------------------------------------------------


if __name__ == '__main__':
    myTree = TreeNode(17)
    print(myTree.val)
    levelOrder(myTree)     # prints the nodes of the tree in breadth-first order, i.e. each level
    myTree = insertIntoBST(myTree, 25)
    print(myTree.right.val)

    levelOrder(myTree)     # prints the nodes of the tree in breadth-first order, i.e. each level
