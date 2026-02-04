from BinaryTree import BinaryTree


def main():
    tree = BinaryTree()

    addingNums = True

    while addingNums:
        num = (
            input("Enter a number to add to the tree (or type stop to stop): ")
        ).lower()
        if num == "stop":
            addingNums = False
        else:
            if num.isdigit():
                tree.add(num)

    tree.print_preorder()
    print("")
    tree.print_inorder()


if __name__ == "__main__":
    main()
