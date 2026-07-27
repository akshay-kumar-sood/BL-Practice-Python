# PROG 5: Transpose Matrix

# Write The Code Here

# PROG 5: Transpose Matrix

# Write The Code Here

# transpose a matrix function
def transpose_matrix(matrix):
  ROWS,COLS=len(matrix),len(matrix[0])
  transpose_matrix=[[0,0,0],[0,0,0],[0,0,0]]

# iterate over row and col
# swap row col
  for row in range(ROWS):
    for col in range(COLS):
      transpose_matrix[row][col]=matrix[col][row]
  
  return transpose_matrix



matrix = [ [1,2,3] , [4,5,6] ,[7,8,9] ]

print(f"Original Matrix : ")

# printing a matrix
for row in matrix:
  print(row)


transposed=transpose_matrix(matrix)

# print transposed matrix
print("Transposed Matrix is : ")
for row in transposed:
  print(row)
