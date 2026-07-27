def multiply_matrix(matrix1, matrix2):

    rows1 = len(matrix1)
    cols1 = len(matrix1[0])

    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    if cols1 != rows2:
        return None

    result = []

    for i in range(rows1):
        row = []

        for j in range(cols2):
            sum = 0

            for k in range(cols1):
                sum += matrix1[i][k] * matrix2[k][j]

            row.append(sum)

        result.append(row)

    return result


# First Matrix

rows1 = int(input("Enter the number of rows for the first matrix: "))
cols1 = int(input("Enter the number of columns for the first matrix: "))

matrix1 = []

print("Enter the first matrix:")

for i in range(rows1):
    row = list(map(int, input(f"Enter row {i + 1} (space-separated values): ").split()))
    matrix1.append(row)


# Second Matrix

rows2 = int(input("Enter the number of rows for the second matrix: "))
cols2 = int(input("Enter the number of columns for the second matrix: "))

matrix2 = []

print("Enter the second matrix:")

for i in range(rows2):
    row = list(map(int, input(f"Enter row {i + 1} (space-separated values): ").split()))
    matrix2.append(row)


result = multiply_matrix(matrix1, matrix2)

if result is None:
    print("Matrix multiplication is not possible.")
else:
    print("Product Matrix:")

    for row in result:
        print(row)