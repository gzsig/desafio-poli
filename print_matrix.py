# A basic code for matrix input from user 

M = int(input("Enter the size of your square matrix:")) 

# Initialize matrix 
matrix = [] 
print("Enter the entries rowwise:") 

numbers = input()
numbers = numbers.split()
if (len(numbers) / M ) != M:
  print("wrong number of arguments")

cont = 0

# For user input 
for i in range(M):     # A for loop for row entries 
  a =[] 
  for j in range(M):   # A for loop for column entries 
    a.append(numbers[j + (cont*M)]) 
  matrix.append(a) 
  cont += 1
  

# For printing the matrix 
for i in range(M): 
  for j in range(M): 
    print(matrix[i][j], end = " ") 
  print() 
