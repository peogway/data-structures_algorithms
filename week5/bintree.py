class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.ismirror = False

    def preorder(self):
        stack = [self.root]
        while stack != []:
            cur = stack.pop(-1)
            if self.ismirror:
                if cur.left is not None:
                    stack.append(cur.left)
                if cur.right is not None:
                    stack.append(cur.right)
            else:
                if cur.right is not None:
                    stack.append(cur.right)
                if cur.left is not None:
                    stack.append(cur.left)
            print(cur.key, end=' ')
        print()

    def search(self, key):
        return self.search_help(self.root, key)

    def search_help(self, node, key):
        if not node:
            return False
        elif node.key > key:
            return self.search_help(node.left, key)
        elif node.key < key:
            return self.search_help(node.right, key)
        else:
            return True

    def insert(self, key):
        self.root = self.insert_help(self.root, key)

    def insert_help(self, node, key):
        if node is None:
            node = Node(key)
        elif node.key > key:
            node.left = self.insert_help(node.left, key)
        elif node.key < key:
            node.right = self.insert_help(node.right, key)
        return node

    def remove(self, key):
        self.root = self.remove_help(self.root, key)

    def getmax(self, node):
        if node.right is None:
            return node.key
        return self.getmax(node.right)

    def removemax(self, node):
        if node.right is None:
            return node.left
        node.right = self.removemax(node.right)
        return node

    def remove_help(self, node, key):
        if node is None:
            return None
        elif node.key > key:
            node.left = self.remove_help(node.left, key)
        elif node.key < key:
            node.right = self.remove_help(node.right, key)
        else:
            if node.right is None:
                return node.left
            elif node.left is None:
                return node.right
            else:
                node.key = self.getmax(node.left)
                node.left = self.removemax(node.left)
        return node

    def postorder(self):
        def postorder_help(node):
            if node:
                if self.ismirror:
                    postorder_help(node.right)
                    postorder_help(node.left)
                else:
                    postorder_help(node.left)
                    postorder_help(node.right)
                print(node.key, end=' ')

        postorder_help(self.root)
        print()

    def inorder(self):
        def inorder_help(node):
            if node:
                if self.ismirror:
                    inorder_help(node.right)
                    print(node.key, end=' ')
                    inorder_help(node.left)
                else:
                    inorder_help(node.left)
                    print(node.key, end=' ')
                    inorder_help(node.right)

        inorder_help(self.root)
        print()

    def breadthfirst(self):
        def printCurrentLevel(root, level):
            if root is None:
                return
            if level == 1:
                print(root.key, end=" ")
            elif level > 1:
                if self.ismirror:
                    printCurrentLevel(root.right, level - 1)
                    printCurrentLevel(root.left, level - 1)
                else:
                    printCurrentLevel(root.left, level - 1)
                    printCurrentLevel(root.right, level - 1)

        h = self.height(self.root)
        for i in range(1, h + 1):
            printCurrentLevel(self.root, i)
        print()

    def height(self, node):
        if node is None:
            return 0
        else:
            lheight = self.height(node.left)
            rheight = self.height(node.right)
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1

    def mirror(self):
        self.ismirror = not self.ismirror


if __name__ == "__main__":
    tree = BST()
    tree.mirror()

    for num in (9, 8, 13, 4, 11, 14, 3, 6, 10, 12, 26, 2, 5, 7, 20, 29):
        tree.insert(num)

    tree.inorder()

    tree.remove(2)
    tree.remove(13)

    tree.preorder()

    tree.mirror()

    for num in (5, 7, 11, 10, 12, 20, 29):
        tree.insert(num)

    tree.preorder()