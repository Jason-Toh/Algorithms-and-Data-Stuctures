'''
Node Data Structure
'''
class Node:
    def __init__(self,data=None,level=None,size=27):
        # Terminal $ at index 0
        self.link = [None] * size
        # Data payload
        self.data = data
        # Level of node
        self.level = level
        #Frequency of of words (may include duplicates)
        self.freq = 0
        #Frequency of unique words (no duplicates)
        self.unique_freq = 0
        #This is for instant teleportation to reach leaf node
        self.get_memory_address = []
        self.string = None
        self.duplicate_count = 0

'''
Trie Data Structure

Downside of Trie compared to Hash Table
1) It wastes memory at every level

Go in plus self.freq
go out plus self.unique.freq
'''
class Trie:
    def __init__(self,text = []):
        self.root = Node()
        for string in text:
            self.insert_recur(string)

    def display(self,key):
        current = self.root
        for char in key:
            index = ord(char) - 97 + 1
            #If path exists
            print("Character: " + str(char))
            if current.link[index] is not None:
                print("Freq: " + str(current.link[index].freq))
                print("Unique Freq: " + str(current.link[index].unique_freq))
                #print("Memory Address: " + str(current.link[index].get_memory_address))
                current = current.link[index]
            #If path does not exist
            else:
                raise Exception(str(key) + " does not exist")
        index = 0
        if current.link[index] is not None:
            current = current.link[index]
        #If path doesn't exist
        else:
            raise Exception(str(key) + " doesn't exist")

    def get_total_freq(self):
        total_freq = 0
        total_unique_freq = 0
        for alpha in self.root.link:
            if alpha is not None:
                total_freq += alpha.freq
                total_unique_freq += alpha.unique_freq
        print("Total number of words: " + str(total_freq))
        print("Total number of unique words: " + str(total_unique_freq))

    #Need to make it sorted somehow
    #Print the output in (pre_order) transversal
    #Pre_order will make it lexicographic order
    #Example
    #[None,None,c,d,None,None,...,z]
    #Loop from a to z
    #Ignoring Nones
    def get_all_strings_with_prefix(self,prefix):
        current = self.root
        for i in range(len(prefix)):
            index = ord(prefix[i]) - 97 + 1
            if current.link[index] is not None:
                current = current.link[index]
            #If path does not exist
            else:
                print("No strings with prefix " + str(prefix) + " exists")
                return
        print("These are strings with prefix: " + str(prefix))
        for memory_address in current.get_memory_address:
            print(memory_address.string)

    #To sort strings lexicographically
    #Perform Pre-Order Transversal
    # This means
    # Visit the parent node
    # Transverse left child node
    # Transverse right child node
    def preOrder(self):
        self.preOrder_aux(self.root)

    def preOrder_aux(self,current,i = -1):
        if i == 0:
            for j in range(current.duplicate_count):
                print(current.string)
            return
        for i in range(len(current.link)):
            if current.link[i] is not None:
                self.preOrder_aux(current.link[i],i)
    
    def insert_recur(self,key,data=None):
        current = self.root
        i = 0
        self.insert_recur_aux(current,key,i,data)

    def insert_recur_aux(self,current,key,i,data = None):
        #base
        if i == len(key):
            index = 0
            value = 0
            #print(index_list)
            if current.link[index] is not None:
                current = current.link[index]  
            #If path does not exist
            else:
                #create a new node
                current.link[index] = Node()
                current.link[index].unique_freq += 1
                current = current.link[index]
                value = 1
            current.duplicate_count += 1
            #Add in the payload
            current.data = data
            #value is for unique frequency
            current.string = key
            return (value,current)
        #recur
        else:
            index = ord(key[i]) - 97 + 1
            #If path exists
            if current.link[index] is not None:
                current = current.link[index]
            #If path does not exist
            else:
                #Create a new node
                current.link[index] = Node()
                current = current.link[index]
            i += 1
            current.freq += 1
            value,leaf_node_memory_address = self.insert_recur_aux(current,key,i,data)
            current.unique_freq += value
            current.get_memory_address.append(leaf_node_memory_address)
            return value,leaf_node_memory_address

    #To print out a binary search tree, need to use recursion

    def search(self,key):
        #Begin from root
        current = self.root
        # go through key 1 by 1
        for char in key:
            #print(current.level)
            #Calculate index
            # $ = 0, a = 1, b = 2, c = 3,...
            index = ord(char) - 97 + 1
            #If path exist
            if current.link[index] is not None:
                current = current.link[index]
            #If path doesn't exist
            else:
                raise Exception(str(key) + " doesn't exist")
        
        #go through the terminal $, index = 0
        index = 0
        #print(current.level)
        if current.link[index] is not None:
            current = current.link[index]
        #If path doesn't exist
        else:
            raise Exception(str(key) + " doesn't exist")
        #now we are at leaf (terminal)
        #print(current.level)
        return current.data

test = Trie()
test.insert_recur("cats")
test.insert_recur("cata")
test.insert_recur("dog")
test.insert_recur("doggy")
test.insert_recur("dogo")
test.insert_recur("dogo")
test.insert_recur("catab")
test.insert_recur("cataa")
test.insert_recur("catsss")
test.insert_recur("cata")
#test.display("dogo")
#test.get_total_freq()
test.get_all_strings_with_prefix("dog")
test.preOrder()
