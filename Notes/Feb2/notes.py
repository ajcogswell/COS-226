## AVL Trees ##

# AVL Trees are: #
# Binary search tree
# self-balancing tree

# AVL Trees have: #
# h = height of the tree
# h = max(h(left), h(right)) + 1

# Traveling up tree #
# -check balance, if unbalanced, rotate
# -if balanced, continue up tree
# -recalc height
# balance = h(left) - h(right)
# acceptable range [-1, 1]

# AVL Tree rotations #
# Left rotation:
#
# (10) bal = 2
#   (20)   h=2
#     (50) h=1
#
# 50 keeps its children, 10 keeps its left child, right child becomes left child of 20
#
# Rotate the 20 node so 10 is oriented on the left
#
#     (20)     bal = 0
# (10)    (50)
#
# Left rotation is for when you're imbalanced on the right
#
#          (a)
#       (c)   (b)
#
# def leftRotate(rootNode(which is A)):
#   set newRoot to B
#   newRoot = rootNode.right
#   rootNode.right = newRoot.left
#   newRoot.left = rootNode
#
#
# Right rotation:
#
#     (50) bal = 2
#   (20)   h=2
# (10)     h=1
#
# Rotate the 20 node so 50 is oriented on the right
#
#     (20)     bal = 0
# (10)    (50)
#
# 10 keeps its children, 50 keeps its right children, left child becomes right child of 20
# Right rotation is for when you're imbalanced on the left
#   (a)   becomes (b)
# (b)               (a)
#
# def rightRotate(rootNode(which is A)):
#   set newRoot to B
#   newRoot = rootNode.left
#   rootNode.left = newRoot.right
#   newRoot.right = rootNode

from BinaryTree import BinaryTree, Node

# Create AVL tree class inheriting BinaryTree


class AVLTree(BinaryTree):
    # overwrite the add

    def add(self, currNode, data):
        if self.head is None:
            self.head = Node(data)
            return

        # CurrNode is our current spot

        if currNode is None:
            # stops recursion
            return Node(data)

        # currNode is a node if we get here

        if currNode == data:
            return currNode  # make no change, iterate up

        if data > currNode.data:
            # set the left to the result of add
            currNode.left = self.add(currNode.left, data)
        else:
            currNode.right = self.add(currNode.right, data)

        # check balance
        # a new node was added, we need to update the height

        left_height = currNode.left.height if currNode.left else 0
        right_height = currNode.right.height if currNode.right else 0
        currNode.height = max(left_height, right_height) + 1

        return currNode


# currNode.left = recursive add cal
# check balance
# if unbalanced, rotate
# update height
# return currNode
#
# currNode <- checking balance of this node
# balance = calcBalance()
#
# if (bal > 1):         # bal = left - right
#   leftB = currNode.left
#   if leftB.balance == 1:
#       slight right lean
#       currNode.left = leftRotate(currNode.left)
#   currNode = rightRotate(currNode)
# elif (leftB.balance < -1):
#       rightB = currNode.right
#   if (rightB.balance == 1):
#       slight left lean
#       currNode.Right = rightRotate(currNode.left)
#   currNode = leftRotate(currNode)
#
## Removing from AVL BST ##
#
# Find next largest or next lowest number
#
#       (50)
#    (25)  (70)
# (10) (30)  (80)
#
# 30 would become root if 50 is deleted, but 70 could also work
#
# def findNextSmallest(nodeToRemove):
#   nextSmall = nodeToRemove.left
#   while(nextSmall.right):
#       nextSmall = nextSmall.right
#   # Next small is in the correct spot
#   return(nextSmall)
#
# def remove(currNode, dataToRemove):
#   if(currNode is None):
#       raise ValueError("Current node is not found.")
#       return None
#   if dataToRemove < currNode.data:
#       currNode.left = remove(currNode.left, dataToRemove)
#   elif dataToRemove > currData.data:
#       currNode.left = remove(currNode.right, dataToRemove)
#   else:
#       if currNode.left and currNode.right:
#           nextSmall = findNextSmallest(currNode)
#           currNode.data = nextSmall.data
#           currNode.left = remove(currNode.left, currNode.data)
#       elif currNode.left:
#           return currNode.left
#       elif currNode.right:
#           return currNode.right
#       else:
#           return None
#   check balance
#   balance = calcBalance(currNode)
#   if balance > 1:
#       leftB = currNode.left
#       if leftB.balance == 1:
#           slight right lean
#           currNode.left = leftRotate(currNode.left)
#       currNode = rightRotate(currNode)
#   elif balance < -1:
#       rightB = currNode.right
#       if rightB.balance == 1:
#           slight left lean
#           currNode.Right = rightRotate(currNode.left)
#       currNode = leftRotate(currNode)
#
#
