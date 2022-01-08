    def sumOfDigits (self, N):
        sum = 0
        while N>0:
            sum += (int(N%10))
            N = N/10;
        
        return sum
