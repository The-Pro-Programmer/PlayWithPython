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
    
def hello():
  print("Stepping into first function")
  for i in range(5):
    print(i)
  
hello()
