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
    q = []      # an empty queue, represented by a list
    print("The root node's value is: ", root.val)
    valuesList = []

    q.append(root)
    print("The queue's first element is now: ", q[0].val)

    currentElement = q.pop(0)

    valuesList.append(currentElement.val)

    print("The list of node values is now: ", valuesList)
    print("The queue is now: ", q)

    # -------------------------------------------------------------------


if __name__ == '__main__':
    myTree = TreeNode(17)
    print(myTree.val)
    levelOrder(myTree)     # prints the nodes of the tree in breadth-first order, i.e. each level
    myTree = insertIntoBST(myTree, 25)
    print(myTree.right.val)