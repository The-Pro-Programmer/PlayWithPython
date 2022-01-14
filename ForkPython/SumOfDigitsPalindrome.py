    def isDigitSumPalindrome(self,N):
        #code here
        sum = 0
        
        while N>0:
            sum += (N%10)
            N = int(N/10)
        
        if(sum<10):
            return 1
        
        rev = 0
        bsum = sum
        while bsum>0:
            rev = (rev*10) + (bsum%10)
            bsum = int(bsum/10)
        
        if(sum==rev):
            return 1
            
        return 0
