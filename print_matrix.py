M = int(input("Enter the size of your square matrix:")) 

# Initialize matrix 
matrix = [] 
numbers = []
one_liner = []
valid = True

while valid:
  print("Enter the entries for the 1 row:") 
  # For user input 
  first_row = (input())
  first_row = first_row.split()
  if len(first_row) != M:
    print("Wrong number of arguments, given {} expected {}".format(len(first_row), M))
    valid = False
  if valid:
    numbers.append(first_row)
    for i in range(M-1):
      print("Enter the entries for the {} row:".format(str(i+2)))
      new_row = (input())
      new_row = new_row.split()
      numbers.append(new_row)
    # create an array with with all numbers
    for row in numbers:
      for number in row:
        one_liner.append(number)
    # print(one_liner)

    # if (len(one_liner) / M ) != M:
    #   print("wrong number of arguments")

    cont = 0


    for i in range(M):     # A for loop for row entries 
      a =[] 
      for j in range(M):   # A for loop for column entries 
        a.append(one_liner[j + (cont*M)]) 
      matrix.append(a) 
      cont += 1
      

    # For printing the matrix 
    print("Entry matrix:")
    for i in range(M): 
      for j in range(M): 
        print(matrix[i][j], end = " ") 
      print() 
  valid =False
