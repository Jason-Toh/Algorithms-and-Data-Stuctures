class Node:
    def __init__(self,key,item = None):
        self.key = key
        self.item = item
        self.left = None
        self.right = None
        self.height = 1

class AVL_Tree:
    def __init__(self):
        self.root = None

    def insert(self,key,item = None):
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
                
            height_of_left_subtree = self.getHeight(current.left)
            height_of_right_subtree = self.getHeight(current.right)
            
            current.height = 1 + max(height_of_left_subtree,height_of_right_subtree)

            balance_factor = height_of_left_subtree - height_of_right_subtree

            #Balance factor = {-1,0,1}

            #Case 1: Left Left
            if balance_factor > 1 and current.key < current.left.key:
                return self.right_rotate(current)

            #Case 2: Right Right
            if balance_factor < -1 and current.key > current.right.key:
                return self.right_rotate(current)

            #Case 3: Left Right
            if balance_factor > 1 and current.key > current.left.key:
                #First rotate the left child and the right of the left child
                current.left = self.left_rotate(current.left)
                return self.right_rotate(current)

            #Case 4: Right Left
            if balance_factor < -1 and current.key < current.left.key:
                #First rotate the right child and the left of the right child
                current.right = self.right_rotate(current.right)
                return self.left_rotate(current)

            return current
        
    def getHeight(self,current):
        if current is None:
            return 0
        else:
            return current.height
                
    def left_rotate(self,current):
        right_of_current = current.right
        left_of_right = right_of_current.left
        
        #Perform Left Rotation
        current.right = left_of_right
        right_of_current.left = right_of_current

        # Update heights 
        current.height = 1 + max(self.getHeight(current.left), self.getHeight(current.right))
        right_of_current.height = 1 + max(self.getHeight(right_of_current.left), self.getHeight(right_of_current.right)) 
  
        # Return the new root 
        return right_of_current 


    def right_rotate(self,current):
        left_of_current = current.right
        right_of_left = left_of_current.left

        #Perform Right Rotation
        current.right = right_of_left
        left_of_current.left = left_of_current

        # Update heights 
        current.height = 1 + max(self.getHeight(current.left), self.getHeight(current.right))
        left_of_current.height = 1 + max(self.getHeight(left_of_current.left), self.getHeight(left_of_current.right)) 
  
        # Return the new root 
        return left_of_current

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

tree = AVL_Tree() 
tree.insert(60) 
tree.insert(20) 
tree.insert(10) 
tree.insert(40) 
tree.insert(50)
tree.insert(35)
tree.insert(25)
print("In Order")
tree.inOrder()
