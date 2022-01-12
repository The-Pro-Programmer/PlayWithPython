    def getCube(ob, n):
        return n*n*n
    
    def armstrongNumber (ob, n):
        # code here 
        backup = n
        sum = 0
        
        while backup>0:
            digit = backup%10
            sum += ob.getCube(digit)
            backup = int(backup/10)
            
        if (sum!=n):
            return "No"
        
        return "Yes"
