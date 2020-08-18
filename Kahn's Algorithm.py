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
        self.edge_list = edge_list
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

    def kahn(self):
        '''
        This topological sort uses breadth first search

        This is known as Kahn's algorithm

        Time Complexity: O(V + E) since its using BFS
        '''
        sorted_list = []

        incoming_edge = [0] * self.V

        #Tracks number of incoming edges
        for edge in self.edge_list:
            u,v = edge
            incoming_edge[v] += 1

        #process is a queue
        process = Queue(self.V)
        for i in range(len(incoming_edge)):
            if incoming_edge[i] == 0:
                process.append(self.vertices[i])

        while process.size() > 0:
            u = process.serve()
            sorted_list.append(u)
            for edge in u.edges:
                incoming_edge[edge.v] -= 1
                if incoming_edge[edge.v] == 0:
                    process.append(self.vertices[edge.v])

        # 0 = False
        # 1 or non-zero = True
        # any() returns True if any of the vertex has incoming edge
        # Eg any([0,0,0,0]) will return False
        # any([0,0,4]) will return True

        #Another one is all()
        #This will return if all elements are True
        #False if otherwise

        #e.g. [0,0,0,0] will return False as 0 is false
        #[0,1,0,2] will return False as not all are true
        #[1,2,3] will return True as all elements are True (non-zero)
        if any(incoming_edge):
            raise Exception("The graph contains cycle")
        return sorted_list

    def dfs_topological_sort(self):
        '''
        This topological sort uses depth first search

        We use two stacks instead of one

        stack is Last In First Out

        Two stacks is First In First Out (Essentially a Queue)

        Time Complexity = O(V + E) because its using depth first search
        '''
        self.reset()
        stack = Stack(self.V)
        for vertex in self.vertices:
            if vertex.visited == False:
                self.dfs_topological_sort_aux(vertex,stack)

        sorted_list = []
        while not stack.is_empty():
            sorted_list.append(stack.pop())
        return sorted_list

    def dfs_topological_sort_aux(self,current_vertex,stack):
        current_vertex.visited = True
        for edge in current_vertex.edges:
            next_vertex = self.vertices[edge.v]
            if next_vertex.visited == False:
                self.dfs_topological_sort_aux(next_vertex,stack)
        stack.push(current_vertex)

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

    def __str__(self):
        #res = "Vertex {}\n".format(self.vertex_id)
        #If you want in alphabetic form
        res = "Vertex {}".format(chr(self.vertex_id+65))
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
        return "U = {}, V = {}, W = {} ".format(self.u,self.v,self.w)

if __name__ == "__main__":
    try:
        vertex_count = 5
        edges = [(0,1),
                 (0,2),
                 (1,3),
                 (2,3),
                 (2,4),
                 (4,3)]
        graph = Graph(vertex_count)
        graph.add_edges(edges,False,True)

        '''
        Kahn's Algorithm (BFS)
        '''
        print("Kahn Algorithm (BFS)")
        kahn = graph.kahn()
        for vertex in kahn:
            print(vertex)
        print("#" * 30)

        '''
        Topological Sort using DFS
        '''
        print("Topological Sort using DFS")
        dfs = graph.dfs_topological_sort()
        for vertex in dfs:
            print(vertex)
        print("#" * 30)
    except Exception as e:
        print(e)