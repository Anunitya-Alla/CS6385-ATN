from collections import defaultdict

class graph:

      # Builds a graph for the given state
    @staticmethod
    def buildG(state : str, numV : int, edges : list[tuple]) -> defaultdict(list):

        def addEdge(u,v):   # Add an edge from vertex u to v
            grph[u].append(v)
            grph[v].append(u)

        grph = defaultdict(list)
        numE = len(edges)
        
        for i in range(numE):   
            if state[i] == '1':
                u = edges[i][0]
                v = edges[i][1]
                addEdge(u,v)

        return grph
    
        # Input the graph built from the current stateand outputs if the graph is connected
    @staticmethod
    def isConn(grph : defaultdict(list), numV : int) -> bool:
        
        traversed = [False for i in range(numV)] # Store if the vertex is visited or not
        stack = []

        traversed[0] = True
        stack.append(0)

        while stack: # Do DFS
            V = stack.pop()
        
            for U in grph[V]:
                if traversed[U] == False:
                    traversed[U] = True
                    stack.append(U)

        if not (False in traversed):
            return True

        return False


        # Input all the possible states and return the states that give a connected graph
    @staticmethod
    def getConnectedComponents(numV : int, edges : list[tuple], PS: list[str]) -> list[str]:

        conn = []
         
        for state in PS:
            grph = graph.buildG(state, numV, edges) # Build a graph for the current state

            if graph.isConn(grph, numV): # check if the graph is connected
                conn.append(state)
        
        return conn
    

    @staticmethod
    def getPS(n : int):

        numPS = int(2 ** n) # Number of all the possible states = 2 ** (number of edges)
        possibleStates = []

        binFormat = '{0:0' + str(n) + 'b}'

        for i in range(numPS):
            
            state = binFormat.format(i) # Convert the integer i to state in binary value
            possibleStates.append(state) # Add te state to the all possible states

        return possibleStates
    
    





    