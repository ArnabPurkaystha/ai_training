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
def getMinor(matrix,row,col):
    minor_matrix = []
    for i in range(len(matrix)):
        if i==row:
            continue
        else:
            row_minor=[]
            for j in range(len(matrix[i])):
                if j==col:
                    continue
                else:
                    row_minor.append(matrix[i][j])
            minor_matrix.append(row_minor)
    return np.array(minor_matrix)

def getDeterminant(matrix):
    if len(matrix)==1:
        return matrix[0][0]
    elif len(matrix)==2:
        return matrix[0,0]*matrix[1,1]-matrix[0,1]*matrix[1,0]
    else:
        det=0
        for col in range(len(matrix[0])):
            det+=((-1)**col)*matrix[0,col]*getDeterminant(getMinor(matrix,0,col))
        return det
def cofactor(matrix):
    size=len(matrix)
    cofactor_matrix=np.zeros((size,size))
    for row in range(size):
        for col in range(size):
            minor=getMinor(matrix,row,col)
            cofactor_matrix[row,col]=((-1)**(row+col))*getDeterminant(minor)
    return cofactor_matrix
def matrix_transpose(matrix):
    size=len(matrix)
    transposed = np.zeros((size, size))
    for j in range(size):
        for i in range(size):
            transposed[j][i] = matrix[i][j]
    return transposed

def adjoint(matrix):
    cofactor_matrix=cofactor(matrix)
    return matrix_transpose(cofactor_matrix)

def inverse(matrix):
    row=matrix.shape[0]
    col=matrix.shape[1]
    if row!=col:
        print("Not a square matrix so, Inverse of the matrix does not exist.")
        return None
    determinant=getDeterminant(matrix)
    if determinant==0:
        print("Determinant is 0 so, Inverse of the matrix does not exist.")
        return None
    else:
        adjoint_matrix=adjoint(matrix)
        inverse_matrix=np.zeros((row,col))
        for i in range(row):
            for j in range(col):
                inverse_matrix[i,j]=adjoint_matrix[i,j]/determinant
        return inverse_matrix
    
def main():
    while True:
        num_of_row,num_of_col =row_column_input()
        if num_of_row ==-1 or num_of_col==-1:
            break
        print("Enter the elements of the matrix:")
        matrix=input_matrix(num_of_row, num_of_col)
        inverse_matrix=inverse(matrix)
        if inverse_matrix is not None:
            print("Inverse of the matrix is:")
            print(inverse_matrix)
        else:
            print("Inverse of the matrix does not exist.")

if __name__ == "__main__":
    main()

