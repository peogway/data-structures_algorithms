# avl.py


class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None
        self.balance = 0


class AVL:
    # Initialize new tree
    def __init__(self) -> None:
        self.root = None
        self.is_balanced = True

    def insert(self, key: int):
        self.root = self.insert_help(self.root, key)


    # Help function for insert
    def insert_help(self, node, key):
        if not node:
            node = AVLNode(key)
            self.is_balanced = False
        elif key < node.key:
            node.left = self.insert_help(node.left, key)
            if not self.is_balanced:                           # Check for possible rotations
                if node.balance >= 0:                       # No Rotations needed, update balance variables
                    self.is_balanced = node.balance == 1
                    node.balance -= 1
                else:                                       # Rotation(s) needed
                    if node.left.balance == -1:
                        node = self.right_rotation(node)    # Single rotation
                    else:
                        node = self.left_right_rotation(node)   # Double rotation
                    self.is_balanced = True
        elif key > node.key:
            node.right = self.insert_help(node.right, key)
            if not self.is_balanced:                      
                if node.balance <= 0:                    
                    self.is_balanced = node.balance == -1
                    node.balance += 1
                else:
                    if node.right.balance == 1:
                        node = self.left_rotation(node)  
                    else:
                        node = self.right_left_rotation(node)  
                    self.is_balanced = True
        return node

    # Single rotation: right rotation around root
    def right_rotation(self, node):
        
        child = node.left                   # Set variable for child node
        node.left = child.right             # Rotate
        child.right = node
        child.balance = node.balance = 0    # Fix balance variables
        return child
    
    def left_rotation(self, node):
        
        
        child = node.right
        node.right = child.left
        child.left = node
        child.balance = node.balance = 0
        return child


    def left_right_rotation(self, node: AVLNode):
        
        
        child = node.left
        grandchild = child.right            # Set variables for child node and grandchild node
        child.right = grandchild.left       # Rotate
        grandchild.left = child
        node.left = grandchild.right
        grandchild.right = node
        node.balance = child.balance = 0    # Fix balance variables
        if grandchild.balance == -1:
            node.balance = 1 
        elif grandchild.balance == 1:
            child.balance = -1
        grandchild.balance = 0
        return grandchild
    
    def right_left_rotation(self, node: AVLNode):
        
        
        child = node.right
        grandchild = child.left
        child.left = grandchild.right
        grandchild.right=child

        node.right = grandchild.left
        grandchild.left = node
        node.balance=child.balance =0

        if grandchild.balance == 1:
            node.balance = -1 
        elif grandchild.balance == -1:
            child.balance = 1
            


        grandchild.balance = 0
        return grandchild

    def preorder(self):
        stack = [self.root]
        while stack != []:
            cur = stack.pop(-1)
            if cur.right is not None:
              stack.append(cur.right)
            if cur.left is not None:
              stack.append(cur.left)

            if cur.balance == -1:
                print(f'{cur.key}-', end=' ')
            elif cur.balance == 1:
                print(f'{cur.key}+', end=' ')
            else:
              print(cur.key, end=' ')
        print()



if __name__ == "__main__":
    Tree = AVL()
    # for key in [9, 10, 11, 3, 2, 6, 4, 7, 5, 1]:
    for key in [9,10,11,3,2,6,4,7,5]:
    # for key in [9,10,11,3,2,6,4]:
        Tree.insert(key)

    Tree1 = AVL()
    # for key in [9, 10, 11, 3, 2, 6, 4, 7, 5, 1]:
    for key in [4, 11, 3, 2, 10, 6, 5, 9, 7]:
    # for key in [9,10,11,3,2,6,4]:
        Tree1.insert(key)
    Tree2 = AVL()
    # for key in [9, 10, 11, 3, 2, 6, 4, 7, 5, 1]:
    for key in [7, 2, 11, 6, 5, 3, 9, 10, 4]:
    # for key in [9,10,11,3,2,6,4]:
        Tree2.insert(key)
    Tree.preorder()
    Tree1.preorder()
    Tree2.preorder()