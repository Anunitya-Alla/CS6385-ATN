#from submission import BuildAG

def genereateAM(print_output=True):
        
    '''
        ------------------------------------------------------------
            Task 2: BUILDING AN ADJACENCY MATRIX FROM UTD-ID
        ------------------------------------------------------------

    '''

    ID = "2021615994"   # Input UTD-ID
    digits = [int(d) for d in ID]   # Convert the ID string to integer array

    bitS = [0 if d%2 ==0 else 1 for d in digits]    # Extract the bit sequence from the digit array
    bitSstr = ''.join(map(str,bitS))
    extBS = bitS * 68   # Extend the bit sequence 68 times

    print(f"The UTD-ID is {ID}")
    print(f"The bit sequence for the above ID is {bitSstr}")

    n = 26  # Total number of vertices 

        # Initialize and populate the matrix
    adjM = [[0 for i in range(n)] for i in range(n)] 

    for i in range(n):
        for j in range(0,n):
            adjM[i][j] = extBS.pop(0)
        
    print("Checking for isolated nodes ... ")

         # Find the isolated nodes and make required changes to the matrix
    cardinality = [sum(adjM[i]) for i in range(n)]

    for node in cardinality:
        if cardinality[node] == 0 :
        
            # Change first position of row and coloumn
            adjM[node][0] = 1
            adjM[0][node] = 1

            #change in last position of row and column
            adjM[node][n-1] = 1
            adjM[n-1][node] = 1
    
    print("Checking for self loops ...")

        # Check diagonal values to prevent any self-loops
    for i in range(n):
        if adjM[i][i] == 1:
            adjM[i][i] = 0
            
        # Make matrix symmetric
    for i in range(n):
        for j in range(i+1,n):
            adjM[j][i] = adjM[i][j]

        # symmetric matrix check 
    print("The matrix is now symmetric") if isSymmetric(adjM) else print("The matrix is not symmetric")

    printM(adjM)    # Print the adjacency matrix

    return adjM

    # Function to print the adjacency matrix
def printM(aM):

    print("Printing the adjacency matrix generated from the given UTD-ID ...")

    print(f"Number of rows: {len(aM)}")
    print(f"Number of columns: {len(aM[0])}")

    for row in aM:
        for i in row:
            print(f"{i:2}", end=" ")  
        print()

    # function to check the if the matrix is symmetric
def isSymmetric(aM):
    rows = len(aM)
    columns = len(aM[0])

    if rows != columns:
        return False

    for i in range(rows):
        for j in range(columns):
            if aM[i][j] != aM[j][i]:
                return False
    return True

    # Function to print task banner
def printB( taskNum, taskDesc):
        banner_width = 60
        taskTitle = f"Task {taskNum}:"
        taskBanner = taskTitle + " " + taskDesc
        bannerLine = "-" * banner_width

        print(bannerLine)
        print(taskBanner.center(banner_width))
        print(bannerLine)

if __name__ == "__main__":

    genereateAM()


