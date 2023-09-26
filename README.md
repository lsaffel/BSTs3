Binary Search Tree methods  

insertIntoBST(node_ptr, val)  
insert a new node with the value val into a binary search tree pointed to by node_ptr  

levelOrder(root_ptr)  
prints the nodes of the tree in breadth-first order, i.e. each level, left to right  
  
reverseLevelOrder(root_ptr)  
prints the nodes of the tree in breadth-first order, i.e. each level, from right to left  

levelOrderCountIt(root_ptr)  
counts and prints how many nodes in the tree have 2 children via level order traversal  

count2ChildrenRec(root_ptr)  
returns the count of the number of nodes in tree with 2 children, recursively  

getHeight(root)  
return the height of a binary tree, recursively  

findMinMaxBST(root)  
find minimum and maximum values in a binary search tree iteratively and print them  

findMin(root)  
find the minimum value iteratively in a binary search tree and return that value  
returns -1 if the tree is empty. Assumes all values in the tree are positive.  

findMax(root)  
find the maximum value iteratively in a binary search tree and return that value  
returns -1 if the tree is empty. Assumes all values in the tree are positive.  

findMinR(root)  
find and return the minimum value in the tree pointed to by root, recursively  
if the tree is empty, return -1. This assumes that the tree has only positive values  

findMaxR(root)  
find and return the maximum value in the tree pointed to by root, recursively  
if the tree is empty, return -1. This assumes that the tree has only positive values  

invertTree(root: TreeNode) -> TreeNode  
inverts a binary tree. That is, reverse the order at each level of the tree  

isPresent(root, value)  
returns boolean True if the value is present in the tree based at root  
and False if it is not  
recursive  

returnTwoValues(a, b)  
a method to test returning two values  

findValue(root: TreeNode, value)  
iterative solution  
returns True or False if found or not found in tree, and a  
pointer to the node above the node where it was found, if it was found  

maxDepth(root) -> int  
returns the maximum depth of a binary tree. It does not have to be a binary search tree.  
Maximum depth is defined as the number of nodes from the root to the lowest leaf.  
depth of a tree is max of (1 + depth of left side) and (1 + right side depth)  
