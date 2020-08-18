class Node:
    def __init__(self, key, item=None, left=None, right=None):
        self.key = key
        self.item = item
        self.left = left
        self.right = right
 
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def __len__(self):
        return self.len_aux(self.root)

    def len_aux(self,current):
        if current is None:
            return 0
        else:
            return 1 + self.len_aux(current.left) + self.len_aux(current.right)

    def insert_iter(self,key,item = None):
        if self.root is None:
            self.root = Node(key,item)
        else:
            current = self.root
            while True:
                if key < current.key:
                    if current.left is None:
                        current.left = Node(key,item)
                        break
                    else:
                        current = current.left
                elif key > current.key:
                    if current.right is None:
                        current.right = Node(key,item)
                        break
                    else:
                        current = current.right
                else:
                    current.item = item
                    break

    def insert_recur(self,key,item = None):
        #Base case at the leaf
        if self.root is None:
            self.root = Node(key,item)
        else:
            self.insert_aux(self.root,key,item)

    def insert_aux(self, current, key, item):
        if key < current.key:
            if current.left is None:
                current.left = Node(key,item)
            else:
                current.left = self.insert_aux(current.left,key,item)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key,item)
            else:
                current.right = self.insert_aux(current.right,key,item)
        else: # key == current.key
            current.item = item
        return current
                                 
    def __contains__(self, key):
        #return self._contains_aux(key, self.root)
        return self.contains_iter(key)

    def contains_iter(self, key):
        current = self.root
        while current is not None:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return True
        return False

    def contains_recur(self,key):
        return self.contains_aux(self.root,key)

    def contains_aux(self, current, key):
        if current is None: # base case: empty
            raise KeyError("key not found")
        elif key == current.key: # base case: found
            return True
        elif key < current.key:
            return self.contains_aux(current.left, key)
        else:#key > current.key
            return self.contains_aux(current.right, key)

    def __getitem__(self, key):
        return self.getitem_iter(key)

    def get_item_iter(self, key):
        current = self.root
        while current is not None:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current.item
        raise KeyError("Key not found")

    def get_item_recur(self,key):
        return self.get_item_aux(self.root,key)

    def get_item_aux(self, current, key):
        if current is None: # base case: empty
            raise KeyError("key not found")
        elif key == current.key: # base case: found
            return current.item
        elif key < current.key:
            return self.get_item_aux(current.left, key)
        else:#key > current.key
            return self.get_item_aux(current.right, key)

    def __setitem__(self, key, item):
        self.set_item_iter(key, item)

    def set_item_iter(self,key,item):
        current = self.root
        while current is not None:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                current.item = item
                return
        raise KeyError("Key not found")

    def set_item_recur(self,key,item):
        self.set_item_aux(self.root,key,item)

    def set_item_aux(self, current, key, item):
        if current is None:
            raise KeyError("Key not found")
        if key < current.key:
            current.left = self.set_item_aux(current.left,key,item)
        elif key > current.key:
            current.right = self.set_item_aux(current.right,key,item)
        else: # key == current.key
            current.item = item
        return current

    def preOrder(self):
        #Vist Parent Node
        #Transverse Left Node
        #Transverse Right Node
        self.preOrder_aux(self.root)

    def preOrder_aux(self,current):
        if current is not None:
            print("{0} ".format(current.key), end="") 
            self.preOrder_aux(current.left)
            self.preOrder_aux(current.right)

    def inOrder(self):
        #Tranverse Left Node
        #Visit Parent Node
        #Transverse Right Node
        self.inOrder_aux(self.root)

    def inOrder_aux(self,current):
        if current is not None:
            self.inOrder_aux(current.left)
            print("{0} ".format(current.key), end="") 
            self.inOrder_aux(current.right)

    def preOrder(self):
        #Vist Parent Node
        #Transverse Left Node
        #Transverse Right Node
        self.preOrder_aux(self.root)

    def preOrder_aux(self,current):
        if current is not None:
            print("{0} ".format(current.key), end="") 
            self.preOrder_aux(current.left)
            self.preOrder_aux(current.right)

    def inOrder(self):
        #Tranverse Left Node
        #Visit Parent Node
        #Transverse Right Node
        self.inOrder_aux(self.root)

    def inOrder_aux(self,current):
        if current is not None:
            self.inOrder_aux(current.left)
            print("{0} ".format(current.key), end="") 
            self.inOrder_aux(current.right)

    def postOrder(self):
        #Transverse Left Node
        #Transverse Right Node
        #Vist Parent Node
        self.postOrder_aux(self.root)

    def postOrder_aux(self,current):
        if current is not None:
            self.postOrder_aux(current.left)
            self.postOrder_aux(current.right)
            print("{0} ".format(current.key), end="") 

tree = BinarySearchTree()
tree.insert_iter(30)
tree.insert_iter(20)
tree.insert_iter(10)
tree.insert_iter(25)
tree.insert_iter(40)
tree.insert_iter(35)
tree.insert_iter(50)
"""The constructed AVL Tree would be 
            30 
           /  \ 
         20    40 
        /  \   / \ 
       10  25 35  50"""
print("PreOrder")
tree.preOrder()
print("")
print("InOrder")
tree.inOrder()
print("")
print("PostOrder")
tree.postOrder()
##tree.set_item_iter("bca",999)
##tree.set_item_iter("abc",888)
##tree.set_item_recur("aac",777)
##tree.set_item_recur("cab",666)
##print(tree.get_item_recur("bca"))
##print(tree.get_item_recur("abc"))
##print(tree.get_item_recur("aac"))
##print(tree.get_item_recur("cab"))
##print(tree.get_item_recur("test"))
##print(tree.contains_recur("bca"))
##print(tree.contains_recur("abc"))
##print(tree.contains_recur("aac"))
##print(tree.contains_iter("cab"))
##print(tree.contains_iter("test"))
