#First Script
print("Hello World")

#Variable declarations
num1 = 4
print(num1)
num2 = 4.5
print(num2)
str1 = "Movie Time"
print(str1)
#List of mixed datatypes
list1 = []
list1.append(num1)
list1.append(num2)
list1.append(str1)
print(list1)

#Input - Output
name = input()
num1 = int(input())
print(name)
print(num1)

#Conditions
if(num1>10):
  print("Greater than 10")
elif(num1<5):
  print("Less than 5")
else:
  print("Else")
  
 def mean(self, N, A):
  sum = 0
  for a in A:
    sum += a
  sum = sum/N
  return int(sum)
    
def hello():
  print("Stepping into first function")
  for i in range(5):
    print(i)
  
hello()

#String functions
S = "AbcdE"
#Converting String to lower case
print(S.lower())
#Print reversed String
print(S[::-1])
#Delete alternate characters from String
print(S[::2])

#Remove Space from String
   def modify(self, s):
        # code here
        op = ""
        for ch in s:
            if(ch!=' '):
                op += ch
        return op

#Count camel case characters in String
    def countCamelCase (self,s):
        # your code here
        count = 0
        i = 0
        for ch in s:
            if(ch>='A' and ch<='Z'):
                count+=1
            i+=1
        return count

#Substring
    def javaSub (ob, S, L, R):
        # code here 
        n = len(S)
        if L<0:
            L = 0
        if R>(n-1):
            R = n-2
        return S[L:R+1]
