    def printFloydTriangle(self, N):
    	#code here 
    	row = 1
    	i = 1
    	while row<=N:
    	    line = ""
    	    for j in  range(row):
    	        line = line + "{} "
    	        line = line.format(i)
    	        i += 1
    	    print(line)
    	    row += 1
