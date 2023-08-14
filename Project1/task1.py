from submission import BuildAG

def main():
        
        '''
        ------------------------------------------------------------
            Task 1: FINDING KCORES OF AN ADJACENCY MATRIX"
        ------------------------------------------------------------

        '''

        k = 2
        adjacency_matrix = [
    [0, 1, 1, 1, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 0, 0],
    [0, 1, 1, 0, 0]
]       

        task1 = BuildAG(adjacency_matrix)   # Build a grph from the input matrix
        task1.printB(1, "FINDING KCORES OF AN ADJACENCY MATRIX") # print banner
        task1.printAG() # print the grph to terminal
        adjM = task1.FindKC0re(adjacency_matrix,k)
        KC0reNodes = set()
        for i in range(len(adjM)):
            if sum(adjM[i]) >= k:
                KC0reNodes.add(i)
            #print(f"{i} degree is {sum(adjM[i])}")
        print(f"{k}-core nodes are {[i for i in KC0reNodes]}")

        task1.printKCN(adjM, k)


if __name__ == "__main__":
    main()
