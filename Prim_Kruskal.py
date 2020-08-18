from MinHeap import MinHeap

def quicksort(array,lo,hi):
    if lo < hi:
        mid = lomuto_partition(array,lo,hi)
        quicksort(array,lo,mid-1)
        quicksort(array,mid+1,hi)
    return array

def lomuto_partition(array,start,end):
    mid = (start + end)//2
    pivot = array[mid][2]
    array[start], array[mid] = array[mid], array[start]
    index = start
    for k in range(start+1,end+1):
        if array[k][2] < pivot:
            index += 1
            array[index],array[k] = array[k],array[index]

    array[start],array[index] = array[index],array[start]
    return index

class UnionFind:
    def __init__(self, size):
        self.parent = [-1] * size

    def find(self, i):
        #finds the root vertex (big boss) of the child vertex (small boss)
        #The big boss is always negative, so the moment we found it, bingo big boss is here
        #Find is O(logV)
        if self.parent[i] < 0: 
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        '''
        Time Complexity of Union: O(V)
        '''
        i = self.find(i)
        j = self.find(j)
        #Ignores if the big boss (root node) of the group are the same
        if i == j: 
            return
        #if parent[i] is bigger (e.g. -2) than parent[j] (e.g -5)
        #Change the big boss for parent[i] to j
        #-5 has 5 five elements whereas -2 has 2 elements
        #So -5 is bigger group than -2 
        if self.parent[i] > self.parent[j]:
            self.parent[i] = j
        elif self.parent[j] > self.parent[i]:
            self.parent[j] = i
        #Once they are the same, increase the member count (e.g -2 -> -3)
        #It has 2 members, now become 3 members
        else:
            self.parent[i] = j
            self.parent[j] -= 1

class Graph:
    def __init__(self,vertex_count):
        #length of vertices
        self.V = vertex_count
        #Create a list of vertices
        self.vertices = [None] * vertex_count
        self.edges = []
        #Initialize the vertices from 0 to vertex_count
        for i in range(vertex_count):
            self.vertices[i] = Vertex(i)

    def __str__(self):
        res = ""
        for vertex in self.vertices:
            res += "{}\n".format(vertex)
        return res

    def reset(self):
        for vertex in self.vertices:
            vertex.discovered = False
            vertex.visited = False
            vertex.distance = 0
            vertex.previous = None

    def add_edges(self,edge_list,weighted,directed):
        for edge in edge_list:
            self.edges.append(edge)
            #If it is weighted, then there should be a third parameter (weight)
            if weighted == True:
                u,v,w = edge
                current_edge = Edge(u,v,w)
            else:
                u,v = edge
                current_edge = Edge(u,v)
            current_vertex = self.vertices[u]
            current_vertex.add_edge(current_edge)
            #If is is undirected, then it is symmetric meaning u -> v and v -> u
            #If directed, then u -> v and v (may or may not) -> u
            if directed == False:
                if weighted == True:
                    u,v,w = edge
                    edge = v,u,w
                    self.edges.append(edge)
                    current_edge = Edge(v,u,w)
                else:
                    u,v = edge
                    current_edge = Edge(v,u)
                current_vertex = self.vertices[v]
                current_vertex.add_edge(current_edge)

    def prim(self,source):
        '''
        Same as dijkstra

        Just change one line:
        v.distance = u.distance + edge.w
        -> v.distance = edge.w

        Time Complexity: O(V log V + E log V)
        Thus, O(E log V)
        '''
        self.reset()
        #source is an index right now
        source = self.vertices[source]
        #Now source is a vertex
        #To keep track of the index in the heap
        discovered = MinHeap(self.V) #discovered is a MinHeap now
        #Add the source to discovered
        discovered.add(source,source.distance) #add(key,data)
        #If want to be sorted by distance, use this
        #result = []
        #Else, use this if want to be sorted by vertex id
        result = [None] * self.V
        index = 0
        while not discovered.is_empty() > 0:
            #if we already have six vertices, we can terminate early
            # if len(result) == self.V:
            #     break
            if index == self.V:
                break
            u = discovered.get_min()[0] #Get the smallest distance from MinHeap
            u.visited = True # means I have visited u
            #u is the current vertex
            #For each edge in the current vertex
            #If want to be sorted by distance, use this
            #result.append(u)
            #Else, use this if want to be sorted by vertex id
            result[u.vertex_id] = u
            index += 1
            for edge in u.edges:
                # edge = (u,v,w)
                v = edge.v
                #Current vertex is now u
                v = self.vertices[v]
                #if v have not been discovered
                if v.discovered == False and v.visited == False:
                    v.discovered = True # means I have discovered v and add it to the minheap
                    #Add the weight from w and distance of u to v
                    v.distance = edge.w
                    discovered.add(v,v.distance)
                    v.previous = u
                #If the vertex has been discovered but not been visited, perform edge relaxation
                elif v.visited == False:
                    #This is edge relaxation
                    #For the edge from the vertex u to the vertex v,
                    #if d[u]+w(u,v)<d[v] is satisfied, update d[v] to d[u]+w(u,v)
                    #If the new distance is less than the current distance from u to v,update it
                    if edge.w < v.distance:
                        v.distance = edge.w
                        discovered.update(v,v.distance)
                        v.previous = u
        return result

    def kruskal(self):
        '''
        Time Complexity:
        * Sorting edges: O(E log E)
        * Initialization of union find: O(V)
        * E log E = E log V^2 = 2 E log V → O(E log V)
        * For loop executes O(E) times
        * The two finds take the same effort as the union, log(v)
        * UNION takes O(V log V) in total
        * FIND takes O(E log V)
        * SORTING takes O(E log E)
        * Total cost: O(E log V + V log V) → O(E log V) 
        '''
        quicksort(self.edges,0,len(self.edges)-1)
        forest = UnionFind(self.V)
        tree = Graph(self.V)
        tree_edge_list = []
        for u,v,w in self.edges:
            if forest.find(u) != forest.find(v):
                forest.union(u,v)
                tree_edge_list.append((u,v,w))
        tree.add_edges(tree_edge_list,True,False)
        return tree

class Vertex:
    def __init__(self,vertex_id):
        #self.vertex_id is the id of the vertex or just the vertex number
        self.vertex_id = vertex_id
        #Each vertex has a list of edges
        self.edges = []
        #When traversing to this edge, discover more vertexes
        self.discovered = False
        #After discovering the nodes, visit one of the discovered nodes
        self.visited = False
        #This is for keeping tracking of distance
        self.distance = 0
        #Backtracking to get a path
        self.previous = None
        #For Colourability
        self.colour = None

    def __str__(self):
        #res = "Vertex {}\n".format(self.vertex_id)
        #If you want in alphabetic form
        res = "Vertex {}\n".format(chr(self.vertex_id+65))
        for edge in self.edges:
            res += "Edge {}\n".format(edge)
        return res

    def add_edge(self,edge):
        self.edges.append(edge)

class Edge:
    def __init__(self,u,v,w=0):
        #In undirected
        # u and v are a pair of vertices
        #In directed
        #u is the starting the vertex
        self.u = u
        #v is the ending vertex
        self.v = v
        #w is the weight between Vertex u and Vertex v
        self.w = w
        
    def __str__(self):
        return "U = {}, V = {}, W = {} ".format(self.u,self.v,self.w)

if __name__ == "__main__":
    vertex_count = 7
    # edges = [(0,1,6),
    #          (0,2,5),
    #          (1,2,3),
    #          (1,3,8),
    #          (2,3,9),
    #          (2,4,2),
    #          (3,4,9)]
    edges = [(0,1,5),
             (0,3,2),
             (1,2,8),
             (1,4,1),
             (2,4,4),
             (3,4,16),
             (3,5,4),
             (4,5,8),
             (4,6,9),
             (5,6,10)]
    g = Graph(vertex_count)
    g.add_edges(edges,True,False)
    source = 0
    print("Prim's Algorithm - Graphs Weighted")
    prim = g.prim(source)
    total_minimum_weight = 0
    for vertex in prim:
        total_minimum_weight += vertex.distance
        print("Vertex Distance from {} to {}: {}".format(chr(65+source),chr(65+vertex.vertex_id),vertex.distance))
        #print("Vertex Distance from {} to {}: {}".format(source,vertex.vertex_id,vertex.distance))
        current_vertex = vertex
        print("The path is")
        while (current_vertex.vertex_id != source):
            print(chr(65+current_vertex.vertex_id))
            #print(current_vertex.vertex_id)
            current_vertex = current_vertex.previous
        print(chr(65+source))
        #print(source)
    print(f'Total Minimum Weight: {total_minimum_weight}')
    print("#"*30)

    kruskal = g.kruskal()
    total_minimum_weight = 0
    print(kruskal)
    
