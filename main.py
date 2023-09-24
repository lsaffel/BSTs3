# started with the code from 34-BSTs

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ---------------------------------------------------------------
def insertIntoBST(node_ptr, val):
    # insert a new node with the value val into a binary search tree pointed to by node_ptr

    # return a new node if the tree is empty
    if node_ptr is None:
        return TreeNode(val)

    if val < node_ptr.val:
        node_ptr.left = insertIntoBST(node_ptr.left, val)
    else:
        node_ptr.right = insertIntoBST(node_ptr.right, val)

    return node_ptr
# ---------------------------------------------------------------


def levelOrder(root_ptr):
    # prints the nodes of the tree in breadth-first order, i.e. each level
    print("Doing a level order traversal of the tree, starting now ----------")
    if root_ptr is None:
        print("The tree is empty")
        return

    q = []      # an empty queue, represented by a list
    valuesList = []         # initialize the list that holds the tree's nodes, traversed breadth first

    q.append(root_ptr)

    while q:        # while q is not empty
        current_node = q.pop(0)     # pop off the first node in the queue (not the last, like a stack)

        # add that node's value to the list
        valuesList.append(current_node.val)

        # check the node's children. If they are not None, add them to the queue
        if current_node.left is not None:
            q.append(current_node.left)
        if current_node.right is not None:
            q.append(current_node.right)

    print("The list of node values is now: ", valuesList)

# ---------------------------------------------------------------


def reverseLevelOrder(root_ptr):
    # prints the nodes of the tree in breadth-first order, i.e. each level, from right to left
    print("Doing a right to left level order traversal of the tree, starting now ----------")
    qRL = []  # an empty queue, represented by a list
    values_list = []  # initialize the list that holds the tree's nodes, traversed breadth first

    if root_ptr is None:
        print("The list of node values is now: ", values_list)
        return

    qRL.append(root_ptr)

    while qRL:  # while q is not empty
        current_node = qRL.pop(0)  # pop off the first node in the queue (not the last, like a stack)

        # add that node's value to the list
        values_list.append(current_node.val)

        # check the node's children. If they are not None, add them to the queue
        # add them this time in right to left order
        if current_node.right is not None:
            qRL.append(current_node.right)
        if current_node.left is not None:
            qRL.append(current_node.left)

    print("The list of node values is now: ", values_list)

# ---------------------------------------------------------------


def levelOrderCountIt(root_ptr):
    # does an iterative (level order traversal and counts all nodes that have 2 children. Returns count.
    # Time Complexity: O(n)
    # Auxiliary Space : O(n) where, n is number of nodes in given binary tree
    print("Doing a count of all nodes with 2 children, starting now ----------")
    q = []  # an empty queue, represented by a list
    # valuesList = []  # initialize the list that holds the tree's nodes, traversed breadth first
    count = 0
    if root_ptr is None:
        return count

    q.append(root_ptr)

    while q:  # while q is not empty. Could use "while len(q) > 0" instead
        current_node = q.pop(0)  # pop off the first node in the queue (not the last, like a stack)

        # if that node has 2 children, increment the count
        if current_node.left is not None and current_node.right is not None:
            count += 1

        # check the node's children. If they are not None, add them to the queue
        if current_node.left is not None:
            q.append(current_node.left)
        if current_node.right is not None:
            q.append(current_node.right)
    return count
# -------------------------------------------------------------------


def count2ChildrenRec(root_ptr):
    # recursively counts all nodes that have 2 children. Returns count.
    # Time Complexity: O(n)
    # Auxiliary Space: O(n)
    if root_ptr is None:
        return 0

    if root_ptr.left is not None and root_ptr.right is not None:
        return 1 + count2ChildrenRec(root_ptr.left) + count2ChildrenRec(root_ptr.right)
    else:
        return count2ChildrenRec(root_ptr.left) + count2ChildrenRec(root_ptr.right)

    # another way to do this, replacing code after the first statement:
    #     res = 0
    #     if (root_ptr.left and root_ptr.right):
    #         res += 1
    #
    #     res += (count2ChildrenRec(root_ptr.left) +
    #             count2ChildrenRec(root_ptr.right))
    #     return res

# -------------------------------------------------------------------

# return the height of a binary tree, recursively


def getHeight(root):
    if root is None:
        return 0
    return 1 + max(getHeight(root.left), getHeight(root.right))
# --------------------------------------------------------------------------------------------------------------------------------------


def findMinMaxBST(root):
    # find minimum and maximum values in a binary search tree iteratively and print them

    # start at the top to find the minimum value
    node_ptr = root
    if node_ptr is None:
        print("The tree is empty. There are no min or max values.")
        return

    # otherwise, continue. The tree is not empty, so find the minimum value first
    # The minimum value is the lowest, left-most node's value
    while node_ptr.left is not None:
        node_ptr = node_ptr.left
    print("The minimum value in the tree is: ", node_ptr.val)

    # start over at the top, to find the maximum value
    # The maximum value is the lowest, right-most node's value
    node_ptr = root
    while node_ptr.right is not None:
        node_ptr = node_ptr.right
    print("The maximum value in the tree is: ", node_ptr.val)

# --------------------------------------------------------------------------------------------------------------------------------------


def findMin(root):
    # find the minimum value iteratively in a binary search tree and return that value
    # returns -1 if the tree is empty. Assumes all values in the tree are positive.
    if root is None:
        print("The tree is empty. Return -1, assuming all values in the tree are positive")
        return -1
    while root.left is not None:
        root = root.left
    return root.val
# --------------------------------------------------------------------------------------------------------------------------------------


def findMax(root):
    # find the maximum value iteratively in a binary search tree and return that value
    # returns -1 if the tree is empty. Assumes all values in the tree are positive.
    if root is None:
        print("The tree is empty. Return -1, assuming all values in the tree are positive")
        return -1
    while root.right is not None:
        root = root.right
    return root.val
# --------------------------------------------------------------------------------------------------------------------------------------


def findMinR(root):
    # find and return the minimum value in the tree pointed to by root, recursively
    # if the tree is empty, return -1. This assumes that the tree has only positive values
    if root is None:
        print("The tree is empty. Return -1")
        return -1
    if root.left is None:
        return root.val
    else:
        return findMinR(root.left)
# --------------------------------------------------------------------------------------------------------------------------------------


def findMaxR(root):
    # find and return the maximum value in the tree pointed to by root, recursively
    # if the tree is empty, return -1. This assumes that the tree has only positive values
    if root is None:
        print("The tree is empty. Return -1")
        return -1
    if root.right is None:
        return root.val
    else:
        return findMaxR(root.right)

# --------------------------------------------------------------------------------------------------------------------------------------


def invertTree(root: TreeNode) -> TreeNode:
    # def invertTree(root):         # this alternate header to the method also works
    # inverts a binary tree. That is, reverse the order of node values at each level of the tree
    # Note - this inverts the tree in place. It does not return a copy of the inverted tree.
    if not root:        # if the root is empty.
        return None     # needed if the tree is empty

    # swap the children, even if a child is None
    root.left, root.right = root.right, root.left

    # swap the children - an alternate way of swapping them, which also works:
    # tmp = root.left
    # root.left = root.right
    # root.right = tmp

    # recursive calls on the children of the root to swap children on each subtree of root
    invertTree(root.left)
    invertTree(root.right)
    return root

# --------------------------------------------------------------------------------------------------------------------------------------


def isPresent(root, value):
    # returns boolean True if the value is present in the tree based at root and False if it is not
    # recursive

    if root is None:    # empty tree
        return False
    if root.val == value:
        return True
    if value < root.val:
        return isPresent(root.left, value)
    else:
        return isPresent(root.right, value)
# --------------------------------------------------------------------------------------------------------------------------------------


def returnTwoValues(a, b):
    # a method to test returning two values
    summ = a + b
    mult = a * b
    return summ, mult
# --------------------------------------------------------------------------------------------------------------------------------------


# def findValue(root: TreeNode, value):
    # returns a pointer to the node above the desired leaf node
    # returns None if the value was not found in the tree or if the tree is empty
    # returns root if the tree has only one node

    # returns boolean valFound as True or False
    # returns a pointer:
    # if it was found, returns pointer to the node above it
    # if it was not found, returns None

    # recursive attempt - does not work
    # if root is None:
    #     return False, None
    # if root.val == value:
    #     # if (root.left is None) and (root.right is None):    # check this in calling function instead?
    #     return True, root   # ??
    #
    # nodeAbovePtr = root     # initialize, to point at the node above the node we're looking for
    # # otherwise, the tree has more than one node and it's not the root node, so keep searching
    # if value < nodeAbovePtr.val:
    #     nodeFound, nodePtr = findValue(nodeAbovePtr.left, value)
    #     return nodeFound, nodePtr
    # else:
    #     nodeFound, nodePtr = findValue(nodeAbovePtr.right, value)
    #     return nodeFound, nodePtr

def findValue(root: TreeNode, value):
    # iterative solution
    # returns True or False if found or not found in tree, and a pointer
    # to the node above the node where it was found, if it was found
    if root is None:        # the tree is empty
        return False, None
    currentNode = root      # initialize
    abovePtr = None     # initialize the pointer to the node above the found node

    # continue. The tree is not empty
    while currentNode is not None:
        if value == currentNode.val:
            return True, abovePtr
        abovePtr = currentNode
        if value < currentNode.val:
            currentNode = currentNode.left
        else:
            currentNode = currentNode.right

    # the node was not found, so it falls out of the loop
    return False, None


# --------------------------------------------------------------------------------------------------------------------------------------


def removeLeaf(root, value):
    # removes the node in a BST which is a leaf node. Returns the root with the leaf node removed
    findValue(value)      # return a pointer to the node above the desired leaf node

# --------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    myTree = TreeNode(17)
    levelOrder(myTree)     # prints the nodes of the tree in breadth-first order, i.e. each level
    myTree = insertIntoBST(myTree, 25)

    levelOrder(myTree)     # prints the nodes of the tree in breadth-first order, i.e. each level

    myTree = insertIntoBST(myTree, 12)
    levelOrder(myTree)     # prints the nodes of the tree in breadth-first order, i.e. each level

    myTree = insertIntoBST(myTree, 6)

    levelOrder(myTree)     # prints the nodes of the tree in breadth-first order, i.e. each level
    #
    myTree = insertIntoBST(myTree, 14)
    levelOrder(myTree)     # prints the nodes of the tree in breadth-first order, i.e. each level

    myTree = insertIntoBST(myTree, 15)
    levelOrder(myTree)     # prints the nodes of the tree in breadth-first order, i.e. each level

    myTree = insertIntoBST(myTree, 23)
    levelOrder(myTree)     # prints the nodes of the tree in breadth-first order, i.e. each level

    reverseLevelOrder(myTree)     # prints the nodes of the tree in breadth-first order, right to left

    levelOrderCountIt(myTree)     # counts num of nodes in the tree have 2 children
                                # via level order traversal
    myTree = insertIntoBST(myTree, 13)
    count = levelOrderCountIt(myTree)     # counts num of nodes in the tree have 2 children
                                # via level order traversal
    print("The number of nodes that have 2 children is: ", count)

    myTree = insertIntoBST(myTree, 5)
    myTree = insertIntoBST(myTree, 10)

    levelOrder(myTree)     # prints the nodes of the tree in breadth-first order, i.e. each level

    count = levelOrderCountIt(myTree)     # counts num of nodes in the tree have 2 children
                                # via level order traversal
    print("The number of nodes that have 2 children is: ", count)

    myTree = insertIntoBST(myTree, 35)
    count = levelOrderCountIt(myTree)     # counts num of nodes in the tree have 2 children
                                # via level order traversal
    print("The number of nodes that have 2 children is: ", count)

    myTree = insertIntoBST(myTree, 600)
    levelOrder(myTree)     # prints the nodes of the tree in breadth-first order, i.e. each level
    count = levelOrderCountIt(myTree)     # counts num of nodes in the tree have 2 children
                                # via level order traversal
    print("The number of nodes that have 2 children is: ", count)

    count = count2ChildrenRec(myTree)   # counts num of nodes in tree with 2 children, recursively
    print("The number of nodes that have 2 children, recursively, is: ", count)

    emptyTree = None
    count = levelOrderCountIt(emptyTree)
    print("The number of nodes that have 2 children is: ", count)
    reverseLevelOrder(emptyTree)

    count = count2ChildrenRec(emptyTree)   # counts num of nodes in tree with 2 children, recursively
    print("The number of nodes that have 2 children, recursively, is: ", count)

    ganglyTree = TreeNode(18)
    ganglyTree.left = TreeNode(10)
    ganglyTree.left.left = TreeNode(5)
    ganglyTree.left.left.left = TreeNode(1)
    ganglyTree.left.left.right = TreeNode(3)
    count = count2ChildrenRec(ganglyTree)  # counts num of nodes in tree with 2 children, recursively
    print("The number of nodes in ganglyTree that have 2 children, recursively, is: ", count)

    count = levelOrderCountIt(ganglyTree)  # counts num of nodes in tree with 2 children, iteratively
    print("The number of nodes in ganglyTree that have 2 children, iteratively, is: ", count)

    ganglyTree.right = TreeNode(30)
    count = count2ChildrenRec(ganglyTree)  # counts num of nodes in tree with 2 children, recursively
    print("The number of nodes in ganglyTree that have 2 children, recursively, is: ", count)

    count = levelOrderCountIt(ganglyTree)  # counts num of nodes in tree with 2 children, iteratively
    print("The number of nodes in ganglyTree that have 2 children, iteratively, is: ", count)

    height = getHeight(emptyTree)
    print("Height of an empty tree is: ", height)

    height = getHeight(myTree)
    print("Height of myTree is: ", height)

    height = getHeight(ganglyTree)
    print("Height of ganglyTree is: ", height)

    findMinMaxBST(emptyTree)
    findMinMaxBST(myTree)
    findMinMaxBST(ganglyTree)

    minn = findMin(myTree)
    print("The minimum value (iteratively) in myTree is: ", minn)

    maximum = findMax(myTree)
    print("The maximum value (iteratively) in myTree is: ", maximum)

    minn = findMinR(myTree)
    print("The minimum value (recursively) in myTree is: ", minn)

    maximum = findMaxR(myTree)
    print("The maximum value (recursively) in myTree is: ", maximum)

    minn = findMinR(ganglyTree)
    print("The minimum value (recursively) in ganglyTree is: ", minn)

    maximum = findMaxR(ganglyTree)
    print("The maximum value (recursively) in ganglyTree is: ", maximum)

    levelOrder(myTree)
    reversedMyTree = invertTree(myTree)
    levelOrder(reversedMyTree)

    print("---------------------------------------------")
    levelOrder(ganglyTree)
    reversedGanglyTree = invertTree(ganglyTree)
    levelOrder(reversedGanglyTree)

    print("----------------- empty tree ----------------------------")
    levelOrder(emptyTree)
    reversedEmptyTree = invertTree(emptyTree)
    levelOrder(reversedEmptyTree)

    # put myTree back to the right order that it was in to begin with, after being inverted above
    reversedEmptyTree = invertTree(myTree)

    levelOrder(myTree)
    isThere = isPresent(myTree, 15)
    print("The value 15 is present within myTree: ", isThere)

    isThere = isPresent(myTree, 24)
    print("The value 24 is present within myTree: ", isThere)

    # tester method to see how to return two values in Python
    summm, multt = returnTwoValues(3, 5)
    print("The sum and multiplied results of 3 and 5 are: ", summm, multt)

    nodeWasFound, nodePtr = findValue(myTree, 23)
    print("The value 23 was found in the tree? ", nodeWasFound)
    if nodePtr is None:
        print("There is no node above")
    else:
        print("The node above the found value contains the value: ", nodePtr.val)

    nodeWasFound, nodePtr = findValue(emptyTree, 23)
    print("The value 23 was found in the tree? ", nodeWasFound)
    if nodePtr is None:
        print("There is no node above")
    else:
        print("The node above the found value contains the value: ", nodePtr.val)

    nodeWasFound, nodePtr = findValue(myTree, 700)
    print("The value 700 was found in the tree? ", nodeWasFound)
    if nodePtr is None:
        print("There is no node above")
    else:
        print("The node above the found value contains the value: ", nodePtr.val)

    nodeWasFound, nodePtr = findValue(myTree, 14)
    print("The value 14 was found in the tree? ", nodeWasFound)
    if nodePtr is None:
        print("There is no node above")
    else:
        print("The node above the found value contains the value: ", nodePtr.val)

    nodeWasFound, nodePtr = findValue(myTree, 17)
    print("The value 17 was found in the tree? ", nodeWasFound)
    if nodePtr is None:
        print("There is no node above")
    else:
        print("The node above the found value contains the value: ", nodePtr.val)

    nodeWasFound, nodePtr = findValue(myTree, 35)
    print("The value 35 was found in the tree? ", nodeWasFound)
    if nodePtr is None:
        print("There is no node above")
    else:
        print("The node above the found value contains the value: ", nodePtr.val)
