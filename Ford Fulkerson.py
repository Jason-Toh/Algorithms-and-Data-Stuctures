from Queue import Queue

class ResidualNetwork:
    def __init__(self,graph,source,sink):
        self.source = source
        self.sink = sink
        self.graph = graph
        self.V = len(graph)
        self.vertices = [Vertex(i) for i in range(self.V)]
        #To store the results of bfs
        self.bfs_result = None
        self.construct_network()
        
    def __str__(self):
        res = ""
        for vertex in self.vertices:
            res += "{}\n".format(vertex)
        return res

    def construct_network(self):
        '''
        Builds the residual network graph
        '''
        for vertex in self.graph.vertices:
            for edge in vertex.edges:
                u,v,capacity,flow = edge.u,edge.v,edge.capacity,edge.flow
                #Calculates the residual capacity
                #Forward edge = residual capacity
                #Backward edge = flow
                residual_capacity = capacity - flow
                #If the flow is not zero, add an edge, because 0 indicates no possible path to travel from vertex u to vertex v
                if residual_capacity != 0:
                    self.vertices[u].add_edge(Edge(u,v,capacity,residual_capacity))
                #If the flow is not zero, add a backward edge
                if flow != 0:
                    self.vertices[v].add_edge(Edge(v,u,capacity,flow,False))
        
    def has_AugmentingPath(self):
        '''
        Checks if there is an available path using BFS
        '''
        self.bfs_result = self.breadth_first_search(self.source)
        return self.bfs_result[self.sink] != None

    def get_AugmentingPath(self):
        '''
        Find an augmenting path

        The idea of Edmonds-Karp is to use BFS in 
        Ford Fulkerson implementation as BFS always 
        picks a path with minimum number of edges
        '''

        #Backtrack to find the the path
        path = []
        current_vertex = self.bfs_result[self.sink]
        while current_vertex.vertex_id != self.source:
            path.append(current_vertex.vertex_id)
            current_vertex = current_vertex.previous
        path.append(self.source)

        #Reverse the path in log n time
        n = len(path)
        for i in range(n//2):
            path[i],path[n-i-1] = path[n-i-1],path[i]

        return path

    def get_smallest_residual_capacity(self):
        '''
        Determines the smallest value in the augmenting path
        '''
        current_vertex = self.bfs_result[self.sink]
        min_residual_capacity = float("inf")
        #Backtrack to find the smallest value in the augmenting path
        while current_vertex.vertex_id != self.source:
            if current_vertex.residual_capacity < min_residual_capacity:
                min_residual_capacity = current_vertex.residual_capacity
            current_vertex = current_vertex.previous
        return min_residual_capacity

    def augmentFlow(self,path,residual_capacity):
        '''
        Augments both flow grapg and residual network
        '''
        self.augmentFlow_flow_graph(path,residual_capacity)
        self.augmentFlow_network(path,residual_capacity)

    def augmentFlow_flow_graph(self,path,residual_capacity):
        for i in range(len(path)-1):
            for j in range(len(self.vertices[path[i]].edges)):
                edge = self.vertices[path[i]].edges[j]
                #Finds the edge from vertex u to vertex v
                if edge.u == path[i] and edge.v == path[i+1]:
                    #Checks the edge whether it is a forward edge or backward edge
                    if edge.forward == True:
                        #If forward augment the edge in the flow graph by adding it
                        #Residual capacity is the smallest value in the augmenting path
                        for k in range(len(self.graph.vertices[path[i]].edges)):
                            edge = self.graph.vertices[path[i]].edges[k]
                            #Terminate early if found the edge
                            if edge.u == path[i] and edge.v == path[i+1]:
                                flow = self.graph.vertices[path[i]].edges[k].flow
                                new_flow = flow + residual_capacity
                                break
                        #Update the flow in the flow graph
                        self.graph.vertices[path[i]].edges[k] = Edge(edge.u,edge.v,edge.capacity,new_flow)
                    else:
                        #if the edge is a backward edge, we have to subtract it
                        for k in range(len(self.graph.vertices[path[i+1]].edges)):
                            edge = self.graph.vertices[path[i+1]].edges[k]
                            #Terminate early if found the edge
                            if edge.u == path[i+1] and edge.v == path[i]:
                                flow = self.graph.vertices[path[i+1]].edges[k].flow
                                new_flow = flow - residual_capacity
                                break
                        #Update the flow in the flow graph
                        self.graph.vertices[path[i+1]].edges[k] = Edge(edge.u,edge.v,edge.capacity,new_flow)

    def augmentFlow_network(self,path,residual_capacity):
        for i in range(len(path)-1):
            delete_lst = []
            for j in range(len(self.vertices[path[i]].edges)):
                edge = self.vertices[path[i]].edges[j]
                #Finds the edge in the residual network that travels from vertex u to vertex v
                if edge.u == path[i] and edge.v == path[i+1]:
                    current_capacity = edge.capacity
                    new_flow = edge.flow - residual_capacity
                    #If the new flow is not zero, update it
                    if new_flow != 0:
                        self.vertices[path[i]].edges[j] = Edge(path[i],path[i+1],current_capacity,new_flow,edge.forward)
                    #Else, destroy the edge, so that there is no possible to travel from vertex u to vertex v
                    else:
                        #WARNING, DO NOT attempt to modify the list while iterating over it (e.g. addition and deletion)
                        #mark the edge for deletion
                        delete_lst.append(j)
                    check = True
                    #Looping through the alternate edge
                    for k in range(len(self.vertices[path[i+1]].edges)):
                        edge = self.vertices[path[i+1]].edges[k]
                        #Update the new edge with the new flow
                        #Terminate early if found the edge
                        if edge.u == path[i+1] and edge.v == path[i]:
                            new_flow = edge.flow + residual_capacity
                            self.vertices[path[i+1]].edges[k] = Edge(path[i],path[i+1],current_capacity,new_flow,edge.forward)
                            check = False
                        break
                    #If the edge does not exist, add a new edge to the list
                    if check:
                        self.vertices[path[i+1]].add_edge(Edge(path[i+1],path[i],current_capacity,residual_capacity,False))
            #Remove all elements in the delete list
            for index in delete_lst:
                self.vertices[path[i]].remove_edge(index)

    def reset(self):
        for vertex in self.vertices:
            vertex.discovered = False
            vertex.visited = False
            vertex.distance = 0
            vertex.previous = None

    def breadth_first_search(self,source):
        self.reset()
        result = [None] * self.V
        source = self.vertices[source]
        discovered = Queue(self.V)
        discovered.append(source)
        while not discovered.is_empty():
            u = discovered.serve()
            u.visited = True
            result[u.vertex_id] = u
            for edge in u.edges:
                v = edge.v
                v = self.vertices[v]
                if v.discovered == False and v.visited == False:
                    discovered.append(v)
                    v.discovered = True # means I have discovered v and add it queue
                    v.residual_capacity = edge.flow
                    v.previous = u       
        return result

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

    def __len__(self):
        return len(self.vertices)

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
                u,v,capacity = edge
                current_edge = Edge(u,v,capacity)
            else:
                u,v = edge
                current_edge = Edge(u,v)
            current_vertex = self.vertices[u]
            current_vertex.add_edge(current_edge)
            #If is is undirected, then it is symmetric meaning u -> v and v -> u
            #If directed, then u -> v and v (may or may not) -> u
            if directed == False:
                if weighted == True:
                    u,v,capacity = edge
                    current_edge = Edge(v,u,capacity)
                else:
                    u,v = edge
                    current_edge = Edge(v,u)
                current_vertex = self.vertices[v]
                current_vertex.add_edge(current_edge)

    def ford_fulkerson(self,source,sink):
        #Initialize flow
        flow = 0
        #Initialize the residual network
        residual_network = ResidualNetwork(self,source,sink)
        #Keep looping as long as there is an augmenting path
        while residual_network.has_AugmentingPath():
            #Get an augmenting path
            path = residual_network.get_AugmentingPath()
            #Get the smallest residual capacity
            smallest_residual_capacity = residual_network.get_smallest_residual_capacity()
            #Augment the flow equal to the residual capacity
            flow += smallest_residual_capacity
            #Updating the residual network
            residual_network.augmentFlow(path,smallest_residual_capacity)
        return flow

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
        #store the residual capacity in a vertex
        self.residual_capacity = None

    def __str__(self):
        #res = "Vertex {}\n".format(self.vertex_id)
        #If you want in alphabetic form
        res = "Vertex {}\n".format(chr(self.vertex_id+65))
        for edge in self.edges:
            res += "Edge {}\n".format(edge)
        return res

    def add_edge(self,edge):
        self.edges.append(edge)

    def remove_edge(self,position):
        self.edges.pop(position)

class Edge:
    def __init__(self,u,v,capacity=0,flow=0,forward=True):
        #In undirected
        # u and v are a pair of vertices
        #In directed
        #u is the starting the vertex
        self.u = u
        #v is the ending vertex
        self.v = v
        #flow between Vertex u and Vertex v
        self.flow = flow
        #capacity between Vertex u and Vertex v
        self.capacity = capacity
        #This is for the residual network to indicate forward and backward edge
        self.forward = forward
        
    def __str__(self):
        return "U = {}, V = {}, flow = {}, capacity = {}, forward_edge = {} ".format(self.u,self.v,self.flow,self.capacity,self.forward)

if __name__ == "__main__":
    #(u,v,flow,capacity)
    # edges = [(0,1,16),
    #          (0,2,13),
    #          (1,2,10),
    #          (1,3,12),
    #          (2,1,4),
    #          (2,4,14),
    #          (3,2,9),
    #          (3,5,20),
    #          (4,3,7),
    #          (4,5,4)]
    # edges = [(0,1,4),
    #          (0,2,6),
    #          (1,3,3),
    #          (2,4,5),
    #          (3,2,3),
    #          (3,5,4),
    #          (4,5,6)]
    # edges = [(0,1,10),
    #          (0,2,10),
    #          (1,2,2),
    #          (1,3,4),
    #          (1,4,8),
    #          (2,4,9),
    #          (3,5,10),
    #          (4,3,6),
    #          (4,5,10)]
    edges = [(0,1,6),
             (0,2,1),
             (0,3,10),
             (1,2,2),
             (1,4,4),
             (1,5,1),
             (2,5,20),
             (3,2,2),
             (3,6,5),
             (4,5,2),
             (4,7,5),
             (5,6,6),
             (5,7,10),
             (6,8,4),
             (7,8,12)]
    source = 0
    sink = 8
    vertex_count = 9
    graph = Graph(vertex_count)
    graph.add_edges(edges,True,True)
    
    max_flow = graph.ford_fulkerson(source,sink)
    print(f"The max flow using ford fulkerson algorithm is {max_flow}")