from submission import BuildAG
from task2  import genereateAM

import contextlib

def main():
    
    '''
        ------------------------------------------------------------
            Task 3: FINDING K-CORES OF THE GENERATED MATRIX"
        ------------------------------------------------------------

    '''
    with contextlib.redirect_stdout(None):  # Redirect print output 
       
        adjM = genereateAM() #  Get matrix from task 2
     # print(adjM)
        n = len(adjM)
    print(adjM[21])

    # adjM[1][21] = 0
    # adjM[21][1] = 0

    print(adjM[21])

    ipM = adjM
    task3 = BuildAG(adjM)
    task3.printKCN(task3.FindKC0re(adjM,10),10)
    
        
    def FindKC0re(aM, k):
        numR = len(aM)
        numC = len(aM[0])
        removed = set()
        while True:
            rowS = [sum(i) for i in aM]
            emptyKC = False
            
            
            for i in range(numR):
                if (rowS[i] < k and  i not in removed):
                    #print(f"removing {i}")
                    removed.add(i)
                    for j in range(numC):
                                
                        aM[i][j] = 0
                        aM[j][i] = 0
                    emptyKC = True
            
            if not emptyKC:
                break
    
        return aM
    
    for k in range(1,n-1):

        #print(adjM[4])
        adjM = FindKC0re(adjM,k)

        KC0reNodes = set()
        for i in range(n):
            if sum(adjM[i]) >= k:
                KC0reNodes.add(i)
                
            # print(f"{i} degree is {sum(adjM[i])}")
        print(f"{k}-core nodes are {[i for i in KC0reNodes]}")

if __name__ == "__main__":
    main()