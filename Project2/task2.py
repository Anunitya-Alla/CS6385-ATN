import matplotlib.pyplot as Mplt
from tabulate import tabulate

from ConnectedComponents import graph
from GetReliablity import reliablity

def plotG(Xvalues, Yvalues): # Plots the p-value Vs Reliablity graph 
    Mplt.plot(Xvalues, Yvalues)
    Mplt.xlabel('p-value')
    Mplt.ylabel('Reliablity')
    Mplt.title('P-value vs Reliablity graph')
    Mplt.grid(True)
    Mplt.show()

def getE(aM, numV): # Returns the list containing tuples (u,v) for rach edge from vertex u to v
      edges = []
      for i in range(numV):
            for j in range(i+1, numV):
                  if aM[i][j] == 1:
                        edges.append((i,j))
      return edges

if __name__ == "__main__":

      aM = [[0,1,1,0,0,1,0],  
            [1,0,1,1,0,0,0],
            [1,1,0,0,1,1,0],
            [0,1,0,0,1,0,0],
            [0,0,1,1,0,0,1],
            [1,0,1,0,0,0,1],
            [0,0,0,0,1,1,0]] # Input adjacency matrix


      numV = len(aM)    # number of vertices

      edgeSUM = 0 
      for i in range(numV):
            edgeSUM += sum(aM[i])

      numE = int(edgeSUM/2)   # number of edges

      edgeList = getE(aM, numV)     # get the list of edges as tuples (u,v)

      possStates = graph.getPS(numE)      # get the list of all possible states in the graph

      connStates = graph.getConnectedComponents( numV, edgeList,possStates)   # get the list of states that give connected graph


      Xvalues = [p/100.0 for p in range(100, 0, -5)]
      Yvalues = []

            # Calculate reliablity for p-value in [0.05,1] 
      for p in range(100, 0, -5):   
            pvalue = p/100.0
            Rscore = reliablity.calcReliablity(connStates, pvalue)
            Yvalues.append(Rscore)


      plotG(Xvalues, Yvalues) # plot the p-value Vs Reliablity graph


            # Print the p-value and Reliablity sum to terminal
      data = []
      for i in range(20):
            data.append([Xvalues[i], Yvalues[i]])
    
      headers = ["p-value", "Reliablity"]
      print(tabulate(data, headers=headers, tablefmt="grid"))

      
      



      





    