class reliablity:

    @staticmethod
    def calcReliablity(connstates : list[str], p: float):   # Calculate reliablity of all the connected states for a given P-value

        Rsum = 0    # store Reliablity sum
        
        for state in connstates:

            Rscore = 1.0

            nums1 = state.count('1') # Count number of edges are UP
            nums0 = state.count('0') # Count number of edges are down

            if nums1 > 0:   # If there exists "UP" edges, then multiply p-value with Rscore and raise it to the power of number of "UP" edges
                Rscore = (Rscore *p) ** nums1 
                
            if nums0 > 0:    # If there exists "DOWN" edges, then multiply (1-p) with Rscore and raise it to the power of number of "DOWN" edges
                Rscore = (Rscore *(1-p))** nums0 

            Rsum = Rsum  + Rscore   # Add the reliablity of each connected state to get combined reliablity sum

        return Rsum

    
    
    
    