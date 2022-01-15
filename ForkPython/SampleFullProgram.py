class Solution:

    def printMinMax(arr):
        max=0
        min=arr[0]
        for a in arr:
            if a>max:
                max = a
            if a<min:
                min=a
                
        print(max, " ", min)
        
    if __name__ == '__main__':
        t = int(input())
        for i in range(t):
            n = int(input())
            arr = list(map(int, input().strip().split()))
            printMinMax(arr)
