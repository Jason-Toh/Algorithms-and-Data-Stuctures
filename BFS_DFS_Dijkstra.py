#Creating an adjency list
from MinHeap import MinHeap
from Queue import Queue
from Stack import Stack

class Graph:
    def __init__(self,vertex_count):
        #length of vertices
        self.V = vertex_count
        #Create a list of vertices
        self.vertices = [None] * vertex_count
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
                    current_edge = Edge(v,u,w)
                else:
                    u,v = edge
                    current_edge = Edge(v,u)
                current_vertex = self.vertices[v]
                current_vertex.add_edge(current_edge)

    def breath_first_search(self,source):
        '''
        Time Complexity is O(V + E)

        Space Complexity is O(V + E) = Adjacency lists

        Adjacent list
        Space Complexity = O(V + E)
        Checking if an edge exists = O(logV) assuming if the array of vertex IDs is sorted
        Retrieve all adjacent vertices of a given vertex = O(X)
        Where X is the number of adjacent neighbours (output-sensitive complexity)

        Adjacency matrix
        Space Complexity = O(V^2)
        Checking if an edge exists = O(1)
        Retrieve all adjacent vertices (neighbours) of a given vertex = O(V)
        Regardless if that neighbour exist or not


        ''' 
        #Reset the discovered and visited = False
        self.reset()
        result = []
        #Source is which vertex you would want to start
        source = self.vertices[source]
        discovered = Queue(self.V) #discovered is a queue
        #Add the source to discovered
        discovered.append(source)
        #For colourability
        source.colour = "Black"
        #O(V) times for adding the vertices to the discovered queue
        while not discovered.is_empty():
            u = discovered.serve()
            u.visited = True # means I have visited u
            result.append(u)
            #When the algorithm finishes, this part is O(E) for the total cost during the run time of breadth first search
            #During runtime, this is just O(k) where k <= E
            #So its not O(E) as we looping all edges of vertex u and not in the whole graph
            for edge in u.edges:
                # edge = (u,v,w)
                v = edge.v
                v = self.vertices[v]
                #if v have not been discovered and v have not been visited
                if v.discovered == False and v.visited == False:
                    if u.colour == "Black":
                        v.colour = "White"
                    else:
                        v.colour = "Black"
                    #Add v to discovered
                    discovered.append(v)
                    v.discovered = True # means I have discovered v and add it queue
        return result

    #What is the shortest distance from source to every other vertexes
    #If unweighted, use breadth first traversal
    #If you want the path itself, use backtracking
    #Does not work for weighted graphs
    def bfs_distance(self,source):
        #Reset the discovered and visited = False
        self.reset()
        result = []
        #Source is which vertex you would want to start
        source = self.vertices[source]
        discovered = Queue(self.V) #discovered is a queue
        #Add the source to discovered
        discovered.append(source)
        while not discovered.is_empty():
            u = discovered.serve() #pop(0) is the same as serve
            u.visited = True # means I have visited u
            result.append(u)
            #When the algorithm finishes, this part is O(E) for the total cost during the run time of breadth first search
            #During runtime, this is just O(k) where k <= E
            #So its not O(E) as we looping all edges of vertex u and not in the whole graph
            for edge in u.edges:
                # edge = (u,v,w)
                v = edge.v
                v = self.vertices[v]
                #if v have not been discovered and v have not been visited
                if v.discovered == False and v.visited == False:
                    #Add v to discovered
                    discovered.append(v)
                    v.discovered = True # means I have discovered v and add it queue
                    v.distance = u.distance + 1
                    v.previous = u       
        return result

    def depth_first_search(self,source):
        '''
        Time Complexity is O(V + E)
        '''
        #Reset the discovered and visited
        self.reset()
        result = []
        #Source is which vertex you would want to start
        source = self.vertices[source]
        discovered = Stack(self.V) #discovered is a stack
        #Add the source to discovered
        discovered.push(source) #append is the same as push
        while not discovered.is_empty():
            u = discovered.pop() #pop last item
            u.visited = True # means I have visited u
            result.append(u)
            #When the algorithm finishes, this part is O(E) for the total cost during the run time of breadth first search
            #During runtime, this is just O(k) where k <= E
            #So its not O(E) as we looping all edges of vertex u and not in the whole graph
            for edge in u.edges:
                # edge = (u,v,w)
                v = edge.v
                v = self.vertices[v]
                #if v have not been discovered and v have not been visited
                if v.discovered == False and v.visited == False:
                    #Add v to discovered
                    discovered.push(v)
                    v.discovered = True # means I have discovered v and add it queue
        return result

    def dfs_recursion(self,source):
        #Reset to make all visited vertex = False
        self.reset()
        result = []
        source = self.vertices[source]
        self.dfs_recursion_aux(source,result)
        return result

    def dfs_recursion_aux(self,current_vertex,result):
        current_vertex.visited = True
        result.append(current_vertex)
        for edge in current_vertex.edges:
            next_vertex = edge.v
            next_vertex = self.vertices[next_vertex]
            if next_vertex.visited == False:
                self.dfs_recursion_aux(next_vertex,result)

    def dijkstra(self,source):
        '''
        Similar to BFS
        - Actually is BFS when the graph is unweighted

        Uses a priority queue
        -Implemented with a min-heap

        O(E * Min_heap.add(key) + V * Min_heap.get_min())
        = O(E * log V + V * log V)
        Time Complexity = O(V log V + E log V) = O(E log V)

        O(Elog V) comes from looping V time in the outer loop and looping in the inner loop
        E = V^2
        So O(V^2logV) = O(ElogV)

        O(V log V) comes from looping V times until heap is empty
        Each time, you update takes O(log V)
        So O(VlogV)

        Time Complexity = O(E log V) for sparse graph
                          O(V^2 log V) for dense graph

        A dense graph is a graph where the number of edges is close to the maximal number of edges
        A sparse graph is a graph in which the number of edges is close to the minimal number of edges. Sparse graph can be a disconnected graph

        where E is for Edge Relaxation
        and log V is for min heap (rise operation)
        #rise is O(log N) so for vertex is O(logV)

        Dijkstra is a
        - Dynamic Programming Algorithm
        - Greedy

        DrawBack: Does not work for negative edges
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
        '''
        result = []
        '''
        #Else, use this if want to be sorted by vertex id
        result = [None] * self.V
        #This part is looping V times, so O(V)
        while not discovered.is_empty():
            #Serving takes O(log V) time
            u = discovered.get_min()[0] #Get the smallest distance from MinHeap
            u.visited = True # means I have visited u
            #u is the current vertex
            #For each edge in the current vertex
            #If want to be sorted by distance, use this
            '''
            result.append(u)
            '''
            #Else, use this if want to be sorted by vertex id
            result[u.vertex_id] = u
            
            #When the algorithm finishes, this part is O(E) for the total cost during the run time of breadth first search
            #During runtime, this is just O(k) where k <= E
            #So its not O(E) as we looping all edges of vertex u and not in the whole graph

            #Each vertex has at most O(V-1) edges so O(V)
            #This will take O(V log V) as looping V times and each time, perform edge relaxation so O(logV)
            for edge in u.edges:
                # edge = (u,v,w)
                v = edge.v
                #Current vertex is now u
                v = self.vertices[v]
                #if v have not been discovered
                if v.discovered == False and v.visited == False:
                    v.discovered = True # means I have discovered v and add it to the minheap
                    #Add the weight from w and distance of u to v
                    v.distance = u.distance + edge.w
                    #This add operation adds the key and performs a rise operation, so O(logV)
                    discovered.add(v,v.distance)
                    v.previous = u
                #If the vertex has been discovered but not been visited, perform edge relaxation
                elif v.visited == False:
                    #This is edge relaxation
                    #For the edge from the vertex u to the vertex v,
                    #if d[u]+w(u,v)<d[v] is satisfied, update d[v] to d[u]+w(u,v)
                    #If the new distance is less than the current distance from u to v,update it
                    if u.distance + edge.w < v.distance:
                        v.distance = u.distance + edge.w
                        #Updating takes O(logV) time
                        discovered.update(v,v.distance)
                        v.previous = u
        return result

    def print_paths(self,graph,source):
        for vertex in graph:
            print("Vertex Distance from {} to {}: {}".format(chr(65+source),chr(65+vertex.vertex_id),vertex.distance))
            current_vertex = vertex
            print("The path is")
            while (current_vertex.vertex_id != source):
                print(chr(65+current_vertex.vertex_id))
                current_vertex = current_vertex.previous
            print(chr(65+source))
        print("#"*30) 
                
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
        # for edge in self.edges:
        #     res += "Edge {}\n".format(edge)
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
        #return "U = {}, V = {}, W = {} ".format(self.u,self.v,self.w)
        return f"U = {self.u}, V = {self.v}, W = {self.w} "

if __name__ == "__main__":
    vertex_count = 4
    my_graph = Graph(vertex_count)
    edges = [(0,1),(0,2),
             (1,2),
             (2,0),(2,3),
             (3,3)]
    # edges = [(0, 1),
    #         (1, 2),
    #         (1, 5),
    #         (2, 5),
    #         (2, 7),
    #         (3, 7),
    #         (4, 8),
    #         (5, 8),
    #         (5, 9),
    #         (6, 10),
    #         (7, 10),
    #         (7, 11),
    #         (8, 12),
    #         (8, 13),
    #         (9, 13),
    #         (10, 11),
    #         (10, 13),
    #         (10, 14),
    #         (10, 15),
    #         (11, 15)]
    # edges = [(0,1),
    #          (0,2),
    #          (1,4),
    #          (1,5),
    #          (2,3),
    #          (4,6),
    #          (4,7),
    #          (5,6),
    #          (6,7)]
    #add_edges(edges,weighted,directed)
    #False for weighted means unweighted
    #False for directed means undirected
    my_graph.add_edges(edges,False,False)
    source = 0
    '''
    Breath-First Search
    '''
    print("Breath-First-Search")
    bfs = my_graph.breath_first_search(source)
    for vertex in bfs:
        print(vertex)
    print("#"*30)
    '''
    Breath-First Search distance
    '''
    bfs_distance = my_graph.bfs_distance(source)
    print("Breath-First-Search-Distance - Graphs UnWeighted")
    my_graph.print_paths(bfs_distance,source)
    '''
    Depth-First-Search Iteration
    '''
    print("Depth-First-Search Iteration")
    dfs = my_graph.depth_first_search(source)
    for vertex in dfs:
        print(vertex)
    print("#"*30)
    '''
    Depth-First-Search Recursion
    '''
    print("Depth-First-Search Recursion")
    dfs = my_graph.dfs_recursion(source)
    for vertex in dfs:
        print(vertex)
    print("#"*30)
    '''
    Dijkstra Algorithm
    '''
    # edges = [(0,1,10),(0,2,5),
    #          (1,2,2),(1,3,1),
    #          (2,1,3),(2,3,9),(2,4,2),
    #          (3,4,4),
    #          (4,3,6)]
    # edges = [(0,1,3),(0,2,18),
    #          (1,3,15),(1,4,5),
    #          (2,6,14),
    #          (3,2,3),(3,5,5),(3,6,6),
    #          (4,3,5),(4,5,11)]
    # edges = [(0,1,3),(0,3,18),
    #          (1,3,14),(1,4,15),(1,2,5),
    #          (2,4,5),(2,5,11),
    #          (3,6,14),
    #          (4,3,3),(4,5,5),(4,6,6),(4,7,10),
    #          (5,7,4),(5,8,11),
    #          (6,9,12),
    #          (7,6,9),(7,8,2),(7,9,1),(7,10,7),
    #          (8,10,4),
    #          (9,10,5)]
    edges = [(0, 1, 1),
            (0, 3, 1),
            (1, 2, 1),
            (1, 4, 6),
            (2, 5, 2),
            (3, 4, 4),
            (3, 6, 1),
            (4, 5, 1),
            (4, 7, 1),
            (5, 8, 4),
            (6, 7, 1),
            (7, 8, 1)]
    # edges = [(0,1,3),
    #          (0,2,5),
    #          (1,2,1),
    #          (1,3,1),
    #          (2,3,5),
    #          (2,4,6),
    #          (3,4,2)]
    # edges = [(0,1,6),
    #          (0,2,1),
    #          (1,4,2),
    #          (2,3,3),
    #          (3,5,1),
    #          (4,5,1)]
    vertex_count = 9
    my_graph = Graph(vertex_count)
    my_graph.add_edges(edges,True,False)
    source = 8
    print("Dijkstra - Graphs Weighted")
    dijkstra = my_graph.dijkstra(source)
    my_graph.print_paths(dijkstra,source)
    
