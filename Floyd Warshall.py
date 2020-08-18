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
        for edge in edge_list:
            self.edges.append(edge)
            if not directed:
                u,v,w = edge
                egde = v,u,w
                self.edges.append(edge)

    def floyd_warshall(self):
        '''
        An all pair shortest algorithm, handles negative weighted edges

        Drawback: Cannot handle negative negatives

        Time Complexity: O(V^3)

        O(V^3) is for the three nested loops

        #If all-pair use Floyd
        #Cause Dijkstra from every vertex
        Time Complexity = O(V) * O(E log V) = O(EV log V) = O(V^3 log V)

        Bellman Ford from every vertex
        Time Complexity = O(V) * O(VE) = O(V^2 E) = O(V^4)

        Hence Floyd is the best for all pairs
        '''
        matrix = [[inf] * self.V for _ in range(self.V)]

        for i in range(self.V):
            matrix[i][i] = 0

        for u,v,w in self.edges:
            matrix[u][v] = w

        #print(*matrix,sep = "\n")

        predecessor = [[None] * self.V for _ in range(self.V)]

        #This is a transitive closure
        #Where if i->k and k->j, then i->j
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    #Edge Relaxation
                    #matrix[i][j] = min(matrix[i][j],matrix[i][k] + matrix[k][j])
                    # if i->k + k->j < i->j
                   if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                       matrix[i][j] = matrix[i][k] + matrix[k][j]
                       predecessor[i][j] = k

        print(*matrix,sep="\n")
        print(*predecessor,sep="\n")

        #Check for negative cycle
        for i in range(self.V):
            if matrix[i][i] != 0:
                raise Exception("Negatice cycle Detected")

        return matrix,predecessor

    def construct_path(self,i,j,predecessor):
        if predecessor[i][j] == None:
            # return [i,j]
            return[chr(i+65),chr(j+65)]
        path1 = self.construct_path(i,predecessor[i][j],predecessor)
        path2 = self.construct_path(predecessor[i][j],j,predecessor)
        path1.pop()
        return path1 + path2

if __name__ == "__main__":
    edges = [(0,2,-2),
             (1,0,4),
             (1,2,3),
             (2,3,2),
             (3,1,-1)]

    # edges = [(0, 1,0),
    #         (1, 2,0),
    #         (1, 5,0),
    #         (2, 5,0),
    #         (2, 7,0),
    #         (3, 7,0),
    #         (4, 8,0),
    #         (5, 8,0),
    #         (5, 9,0),
    #         (6, 10,0),
    #         (7, 10,0),
    #         (7, 11,0),
    #         (8, 12,0),
    #         (8, 13,0),
    #         (9, 13,0),
    #         (10, 11,0),
    #         (10, 13,0),
    #         (10, 14,0),
    #         (10, 15,0),
    #         (11, 15,0)]
    
    vertex_count = 4
    my_graph = Graph(vertex_count)
    my_graph.add_edges(edges,True)
    matrix,predecessor = my_graph.floyd_warshall()

    for i in range(vertex_count):
        for j in range(vertex_count):
            # print("Source: {}".format(chr(i+65)))
            # print("Destination: {}".format(chr(j+65)))
            print("Distance from source {} to destination {} is {}".format(chr(i+65),chr(j+65),matrix[i][j]))
            path = my_graph.construct_path(i,j,predecessor)
            print(f"The path from source {chr(i+65)} to {chr(j+65)} is {path}\n")
