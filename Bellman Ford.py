from math import inf

class Graph:
    def __init__(self,vertex_count):
        self.V = vertex_count
        self.edges = []

    def __str__(self):
        res = ""
        for vertex in self.edges:
            res += "Vertex {}\n".format(vertex)
        return res

    def add_edges(self,edge_list,directed = True):
        '''
        This an edge list representation
        '''
        for edge in edge_list:
            self.edges.append(edge)
            if not directed:
                u,v,w = edge
                egde = v,u,w
                self.edges.append(edge)

    def bellman_ford(self,source):
        '''
        This algorithm is for graphs with negative edges

        #If no negative edges, use dijkstra

        To overcome negative edges, we have to consider all edges
        This means bellman ford is no longer greedy unlike dijkstra

        2 main components
        - Distance Calculation
        - Check for negative cycle

        Time Complexity: O(VE)

        O(V) to initialize distance and predecessor

        Calculate distance
        O(V) outer loop
        O(E) inner loop

        Check Negative cycle
        O(E) one last time

        Drawback: Does not work for negative cycles (actually raises an Exception)
        '''
        distance = [inf] * self.V #O(V)
        predecessor = [None] * self.V #O(V)
        distance[source] = 0

        #If there are five vertices, at max there are at most 4 edges without a cycle
        for i in range(self.V-1): #O(V)
            print(distance)
            for u,v,w in self.edges: #O(E)
                if distance[v] > distance[u] + w:
                    distance[v] = distance[u] + w
                    predecessor[v] = u

        print(distance)
                    
        #Check for negative cycles           
        for u,v,w in self.edges: #O(E)
            #If a number becomes smaller, a negative cycle exist
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                print(distance)
                raise Exception("Graph contains negative-weight cycles")
        return distance,predecessor
    
if __name__ == "__main__":
    try:
        #This list has a negative cycle
        # edges = [(0,1,5),(0,2,8),
        #         (1,3,3),
        #         (2,1,-4),
        #         (3,4,-1),
        #         (4,2,-1)]
        edges = [(0, 1, -1),(0, 2, 4),
                 (1, 2, 3), (1, 3, 2), (1, 4, 2),
                 (3, 2, 5),(3, 1, 1),
                 (4, 3, -3)]
        # edges = [(0,1,5),(0,2,6),
        #          (1,3,-1),
        #          (2,1,4),(2,4,-10),
        #          (3,2,-2),(3,4,4),(3,5,3),
        #          (4,6,-6),
        #          (5,4,-5),
        #          (6,5,10)]
        vertex_count = 5
        my_graph = Graph(vertex_count)
        my_graph.add_edges(edges,True)
        '''
        Bellman-Ford Algorithm
        '''
        source = 0
        distance,predecessor = my_graph.bellman_ford(source)
        print("Source: {}".format(chr(source+65)))
        print("Distance from source is {}".format(distance[source]))
        print("Predecessor from source is {}".format(predecessor[0]))
        print("#" * 30)
        for i in range(1,len(distance)):
            print("Distance from {} to {}: {}".format(chr(65+source),chr(65+i),distance[i]))
            print("Predecessor of {}: {}".format(chr(i+65),chr(65+predecessor[i])))
            print("#" * 30)
    except Exception as e:
        print(e)
