class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    # initialize Tree
    def __init__(self):
        # we have no nodes yet in the tree
        self.head = None

    def add(self, data):
        # if it's not already in the tree, we'll add.

        newNode = Node(data)

        if self.head is None:
            # tree doesn't have a root/head node
            self.head = newNode
            return  # done

        # traverse the tree until we find the correct position
        currNode = self.head  # Set pointer to look at start
        posFound = False

        while not posFound:
            if currNode.data == newNode.data:
                # Node with this data already exists, do not add
                return
            elif currNode.data > newNode.data:
                # Go left
                if currNode.left is None:
                    currNode.left = newNode
                    posFound = True
                else:
                    currNode = currNode.left
            elif currNode.data < newNode.data:
                # Go right
                if currNode.right is None:
                    currNode.right = newNode
                    posFound = True
                else:
                    currNode = currNode.right

    def inorder_print(self, node):
        if node is None:  # stops the recursion
            return

        self.inorder_print(node.left)
        if node.data is not None:
            print(node.data, end=",")
        self.inorder_print(node.right)

    def preorder_print(self, node):
        # prints all nodes, pre order
        if node is None:  # stops the recursion
            return

        if node.data is not None:
            print(node.data, end=",")
        self.preorder_print(node.left)
        self.preorder_print(node.right)

    def print_inorder(self):
        # Helper method to start in-order traversal from the head
        self.inorder_print(self.head)

    def print_preorder(self):
        # Helper method to start pre-order traversal from the head
        self.preorder_print(self.head)
