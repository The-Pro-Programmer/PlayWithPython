    #Function to return list of integers visited in snake pattern in matrix.
    def snakePattern(self, matrix): 
       # code here 
       n = len(matrix[0])
       nums = []
       total = n*n
       count = 0
       r = 0
       c = 0
       right = 0
       while count<total:
           nums.append(matrix[r][c])
           count+=1
           
           if(count%n==0):
               r+=1
               
               if r%2==0:
                   right = 0
                   c = -1
               else:
                   right = 1
                   c = n
           
           if right==0:
                c += 1
           else:
                c -= 1
      
       return nums
