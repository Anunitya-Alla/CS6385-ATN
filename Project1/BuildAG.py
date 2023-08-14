import networkx as nx
import matplotlib.pyplot as plt

from collections import defaultdict


class BuildAG:

    def __init__(self, aM) -> None:

        self.g = defaultdict(list)

        num_vertices = len(aM)


        for i in range(num_vertices):
            for j in range(num_vertices):
                if aM[i][j] == 1:
                    self.addAE(i,j)
        
        self.printAG()

    
    def addAE(self, vertexU, vertexV):
        self.g[vertexU].append(vertexV)
                    
    def printAG(self):
        print("List of Vertices:", list(self.g.keys()))
        print("Edges:")
        for node, neighbors in self.g.items():
            for neighbor in neighbors:
                print(f"{node} - {neighbor}")
        

        G = self.convert_to_networkx_graph()
        pos = nx.spring_layout(G)  # Determine the layout of the graph
        nx.draw(G, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=12, font_color="black", edge_color="gray", width=2)

        # Display the graph
        plt.show()

    def convert_to_networkx_graph(self):
        graph = nx.Graph()

        for node, neighbors in self.g.items():
            for neighbor in neighbors:
                graph.add_edge(node, neighbor)

        return graph

    def findKC(self, k):

        traverse = set()

        d = defaultdict(int)
        d = [len(self.g[i]) for i in self.g.keys()]

        [self.traversal(traverse, d, i, k) for i in self.g.keys() if i not in traverse]


        for i in self.g.keys():
            if d[i] >= k:
                print("[" + str(i)+ "]", end = " ")
            for j in self.g[i]:
                if d[j] >= k:
                        print("-> " + str(j), end=" ")
 
                print()

    def traversal(self, traversed, d , node, k):
        
        traversed.add(node)

        for i in self.g[node]:
            print("node" + str(node) + " i " + str(i))
            if d[node] < k: 
                d[i] = d[i] - 1
            
            if i not in traversed:
                self.traversal(traversed, d, i, k)
    
if __name__ == "__main__":

    adjacency_matrix = [
    [0, 1, 1, 1, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0]
]
    #buildAG =  BuildAG(adjacency_matrix)
    

            
        

    
                   



        



'''
Algorithm to find the k-core
1. Delete all nodes of degree < k.
2. If the remaining g is empty, then output the message “the k-core
is empty” and halt.
3. If the remaining g is non-empty, then
• If every node in the remaining g has degree ≥ k, then this is
the k-core; output this g and halt.
• Else repeat from Step 1.

'''

    


'''
g1 = Buildg()
g1.buildAg(adjacency_matrix)
g1.printAg()
g1.findKC(3)

'''


adjM = [[0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1], 
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0], 
        [0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1], 
        [1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1], 
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0], 
        [1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1], 
        [1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0], 
        [1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1], 
        [1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1], 
        [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0], 
        [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1], 
        [0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0], 
        [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1], 
        [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1], 
        [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0], 
        [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1], 
        [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
          [1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1], 
          [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
            [0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0], 
            [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1], 
            [0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0], 
            [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1], 
            [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1], 
            [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0], 
        [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0]]     
print(len(adjM))







buildAG =  BuildAG(adjM)
print(adjM([19]))
print(adjM([20][20]))

