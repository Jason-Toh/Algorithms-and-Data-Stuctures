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

'''
Trie Data Structure

Downside of Trie compared to Hash Table
1) It wastes memory at every level
'''
class Trie:
    def __init__(self):
        self.root = Node(level=0)

    def insert_iter(self,key,data=None):
        count_level = 1
        #Begin from root
        current = self.root
        #Go through the key 1 by 1
        for char in key:
            #Calculate index
            # $ = 0, a = 1, b = 2, c = 3,...
            index = ord(char) - 97 + 1
            #If path exists
            if current.link[index] is not None:
                current = current.link[index]
            #If path does not exist
            else:
                #Create a new node
                current.link[index] = Node(level=count_level)
                current = current.link[index]
            count_level += 1
        #Go through the terminal $, index = 0
        index = 0
        if current.link[index] is not None:
            current = current.link[index]
        #If path does not exist
        else:
            #create a new node
            current.link[index] = Node(level=count_level)
            current = current.link[index]
        #Add in the payload
        current.data = data

    def insert_recur(self,key,data=None):
        current = self.root
        i = 0
        self.insert_recur_aux(current,key,i,data)

    def insert_recur_aux(self,current,key,i,data=None):
        #base
        #When we're at the leaf node
        #i == ?
        if i == len(key):
            #What happend when I gone through all of my alphabets in key
            index = 0
            if current.link[index] is not None:
                current = current.link[index]
            #If path does not exist
            else:
                #create a new node
                current.link[index] = Node()
                current = current.link[index]
            #Add in the payload
            current.data = data
            return
        #recur
        else:
            #Calculate index
            # $ = 0, a = 1, b = 2, c = 3,...
            index = ord(key[i]) - 97 + 1
            #If path exists
            if current.link[index] is not None:
                current = current.link[index]
            #If path does not exist
            else:
                #Create a new node
                current.link[index] = Node()
                current = current.link[index]
                #Doing key[1:] is bad, noob, minus marks
                #key[1:] means we're removing the first letter, leaving the second,third,fourth so on and so forth
                #self.insert_recur_aux(current,key[1:],data)
            #Alternative is key[i]
            i += 1
            self.insert_recur_aux(current,key,i,data)

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
test.insert_iter("lol","123")
test.insert_iter("loa","456")
test.insert_iter("lol","789")
test.insert_iter("uwu",None)

try:
    print(test.search("lol"))
except Exception as e:
    print(e)
    
try:
    print(test.search("loa"))
except Exception as e:
    print(e)
    
try:
    print(test.search("los"))
except Exception as e:
    print(e)
    
try:
    print(test.search("lo"))
except Exception as e:
    print(e)
    
try:
    print(test.search("uwu"))
except Exception as e:
    print(e)
