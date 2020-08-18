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

'''
Trie Data Structure

Downside of Trie compared to Hash Table
1) It wastes memory at every level

Go in plus self.freq
go out plus self.unique.freq
'''
class Trie:
    def __init__(self,suffixes = []):
        self.root = Node()
        for suffix in suffixes:
            self.insert_recur(suffix)

    def display(self,key):
        current = self.root
        for char in key:
            index = ord(char) - 97 + 1
            #If path exists
            print("Character: " + str(char))
            if current.link[index] is not None:
                print("Freq: " + str(current.link[index].freq))
                print("Unique Freq: " + str(current.link[index].unique_freq))
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
    
    def insert_recur(self,key,data=None):
        current = self.root
        i = 0
        self.insert_recur_aux(current,key,i,data)

    def insert_recur_aux(self,current,key,i,data=None):
        #base
        if i == len(key):
            index = 0
            value = 0
            if current.link[index] is not None:
                current = current.link[index]
            #If path does not exist
            else:
                #create a new node
                current.link[index] = Node()
                current.link[index].unique_freq += 1
                current = current.link[index]
                value = 1
            #Add in the payload
            current.data = data
            return value
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
            value = self.insert_recur_aux(current,key,i,data)
            current.unique_freq += value
            return value

    #To print out a binary search tree, need to use recursion

    def search(self,key):
        #Begin from root
        current = self.root
        # go through key 1 by 1
        for char in key:
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

def generate_suffixes(string):
    #Complexity is O(N^2)
    #There are N suffixes
    #Every suffix is as long as 1 all the way up to N
    #So total complexity is O(N^2)
    suffix_list = []
    for i in range(len(string)):
        suffix_list.append(string[i:])
    return suffix_list

string = "banananas"
suffix_array = generate_suffixes(string)
test = Trie(suffix_array)
test.get_total_freq()
test.display("anananas")
