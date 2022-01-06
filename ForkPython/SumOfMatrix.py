    
    def sumOfMatrix(self,N,M,Grid):
        sum = 0
        for n in range(N):
            for m in range(M):
                sum += Grid[n][m]
        return sum
