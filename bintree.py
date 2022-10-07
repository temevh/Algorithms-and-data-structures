class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        curr = self.root
        while(True):
            if(key < curr.key):
                if not curr.left:
                    curr.left = Node(key)
                    break
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = Node(key)
                    break
                curr = curr.right

    def preorder(self):
        root = self.root
        self.orderhelper(root)       
        print()

    def orderhelper(self, root):
        if root == None:
            return None
        print(root.key, end=' ')
        self.orderhelper(root.left)
        self.orderhelper(root.right)
        
    def search(self, key):
        if self.root is None:
            self.root = Node(key)
            return True
        else:
            curr = self.root
            while(True):
                if curr == None:
                    return False
                elif curr.key == key:
                    return True
                if curr.key > key:
                    if curr.left == key:
                        return True
                    else:
                        curr = curr.left
                elif curr.key < key:
                    if curr.right == key:
                        return True
                    else:
                        curr = curr.right

    def getmin(self, node):
        current = node
        while(current.right is not None):
            current = current.right

        return current
    
    def remove(self, key):
        root = self.root
        self.removehelper(root, key)

    def removehelper(self, root, key):
        if root == None:
            return root
        
        if key < root.key:
            root.left = self.removehelper(root.left, key)
        elif key > root.key:
            root.right = self.removehelper(root.right, key)
        else:
            if root.left == None:
                temp = root.right
                root = None
                return temp
            elif root.right == None:
                temp = root.left
                root = None
                return temp
            temp = self.getmin(root.left)
            root.key = temp.key
            root.left = self.removehelper(root.left, temp.key)
        return root
    
    def breadthfirst(self):
        root = self.root
        self.printLeverOrder(root)
        print()

    def printLeverOrder(self,root):
        h = self.height(root)
        for i in range(1,h+1):
            self.printCurrentLevel(root, i)
    
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
    
    def printCurrentLevel(self, root, level):
        if root is None:
            return
        if level == 1:
            print(root.key, end=" ")
        elif level > 1:
            self.printCurrentLevel(root.left, level-1)
            self.printCurrentLevel(root.right, level-1)


if __name__ == "__main__":
    Tree = BST()
    keys = [5, 9, 1, 3, 7, 4, 6, 2]
    for key in keys:
        Tree.insert(key)

    Tree.preorder()         # 5 1 3 2 4 9 7 6
    Tree.breadthfirst()     # 5 1 9 3 7 2 4 6
    