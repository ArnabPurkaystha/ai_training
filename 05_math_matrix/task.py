import numpy as np
def row_column_input():
    check=True
    while check:
        try:
            num_of_row=int(input("Enter number of rows:"))
            num_of_col=int(input("Enter number of columns:"))
            check=False
        except ValueError as e:
            print(f"Error: {e}.")
    return (num_of_row, num_of_col)

def input_matrix(num_rows, num_cols):
    matrix = []
    i = 0
    while i < num_rows:
        try:
            row = list(map(int, input(f"Row {i+1}, enter values separated by space( {num_cols}): ").split()))
            if num_cols != len(row):
                raise ValueError(f"wanted {num_cols} values but got {len(row)} values")
            matrix.append(row)
            i += 1  
        except ValueError as e:
            print(f"Error: {e}. Please re-enter Row {i+1}.")
    return np.array(matrix)

def matrix_subtraction():
    num_of_row,num_of_col =row_column_input()
    print("Enter the elements of the first matrix:")
    matrix1=input_matrix(num_of_row, num_of_col)
    print(matrix1)
    print("Enter the elements of the second matrix:")
    matrix2=input_matrix(num_of_row, num_of_col)
    print(matrix2)
    result=np.zeros((num_of_row, num_of_col))
    for i in range(num_of_row):
        for j in range(num_of_col):
            result[i][j]=matrix1[i][j]-matrix2[i][j]
    return result

def scalar_multiplication():
    num_of_row,num_of_col =row_column_input()
    print("Enter the elements of the matrix:")
    matrix=input_matrix(num_of_row, num_of_col)
    print(matrix)
    scalar=int(input("Enter scalar value:"))
    result=np.ones((num_of_row, num_of_col))
    for i in range(num_of_row):
        for j in range(num_of_col):
            result[i][j]=matrix[i][j]*scalar
    return result

def matrix_multiplication():
    first_matrix_row, first_matrix_column= row_column_input()
    print("Enter the elements of the first matrix:")
    matrix1=input_matrix(first_matrix_row, first_matrix_column)
    print(matrix1)
    second_matrix_row, second_matrix_column= row_column_input()
    print("Enter the elements of the second matrix:")
    matrix2=input_matrix(second_matrix_row, second_matrix_column)
    print(matrix2)
    if first_matrix_column == second_matrix_row:
        result=np.ones((first_matrix_row, second_matrix_column))
        for i in range(first_matrix_row):
            for j in range(second_matrix_column):
                result[i][j]=sum([i * j for i, j in zip(matrix1[i,:], matrix2[:,j])])
        return result
    else:
        return np.array([])

def matrix_transpose():
    rows,cols=row_column_input()
    print("Enter the elements of the first matrix:")
    matrix=input_matrix(rows, cols)
    print(matrix)
    transposed = np.zeros((cols, rows))
    for j in range(cols):
        for i in range(rows):
            transposed[j][i] = matrix[i][j]
    return transposed

def is_identity_matrix():
    rows,cols=row_column_input()
    print("Enter the elements of the matrix:")
    matrix=input_matrix(rows, cols)
    print(matrix)
    if rows != cols:
        return False
    for i in range(rows):
        for j in range(cols):
            if i == j:
                if matrix[i][j] != 1:  
                    return False
            else:
                if matrix[i][j] != 0: 
                    return False
    return True
def menu():
    while True:
        print("\nMatrix Operations Menu:")
        print("1. Input Matrix")
        print("2. Matrix Subtraction")
        print("3. Scalar Multiplication")
        print("4. Matrix Multiplication")
        print("5. Matrix Transpose")
        print("6. Check if Matrices are Identical")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            rows,cols=row_column_input()
            matrix=input_matrix(rows, cols)
            print("Matrix entered:")
            print(matrix)
        elif choice == '2':
            print("Performing matrix subtraction...")
            result = matrix_subtraction()
            print("Result of subtraction:")
            print(result)
        elif choice == '3':
            print("Performing scalar multiplication...")
            result = scalar_multiplication()
            print("Result of scalar multiplication:")
            print(result)
        elif choice == '4':
            print("Performing matrix multiplication...")
            result = matrix_multiplication()
            if len(result)!=0:
                print("Result of multiplication:")
                print(result)
            else:
                print("Dimension mismatch, Multiplication not possible")
        elif choice == '5':
            print("Performing matrix transpose...")
            result = matrix_transpose()
            print("Transpose of the matrix:")
            print(result)
        elif choice == '6':
            print("Checking if matrice is an identity matrix...")
            result = is_identity_matrix()
            print("matrix is identity" if result else "Matrix is not identity.")
        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    menu()