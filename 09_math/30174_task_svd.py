import numpy as np

def row_column_input():
    check = True
    while check:
        try:
            num_of_row = int(input("Enter number of rows: "))
            num_of_col = int(input("Enter number of columns: "))
            check = False
        except ValueError as e:
            print(f"Error: {e}.")
    return num_of_row, num_of_col

def input_matrix(num_rows, num_cols):
    matrix = []
    i = 0
    while i < num_rows:
        try:
            row = list(map(int, input(f"Row {i+1}, enter values separated by space ({num_cols}): ").split()))
            if num_cols != len(row):
                raise ValueError(f"Expected {num_cols} values but got {len(row)} values.")
            matrix.append(row)
            i += 1  
        except ValueError as e:
            print(f"Error: {e}. Please re-enter Row {i+1}.")
    return np.array(matrix)

def is_svd_possible(matrix):
    if matrix.size == 0:
        print("Matrix is empty!")
        return False
    if len(matrix.shape) != 2:
        print("Matrix is not 2D!")
        return False
    return True

def calculate_eigenvalues_and_vectors(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors

def svd_decomposition(A):
    AtA = np.dot(A.T, A)
    eigenvalues_AtA, V = calculate_eigenvalues_and_vectors(AtA)
    singular_values = np.sqrt(np.abs(eigenvalues_AtA))
    sorted_indices = np.argsort(singular_values)[::-1]
    singular_values = singular_values[sorted_indices]
    V = V[:, sorted_indices]
    m, n = A.shape
    Sigma = np.zeros((m, n))
    np.fill_diagonal(Sigma, singular_values)
    U = np.zeros((m, m))
    for i in range(len(singular_values)):
        if singular_values[i] > 1e-10:
            U[:, i] = (1 / singular_values[i]) * np.dot(A, V[:, i])
    return U, Sigma, V.T

def verify_svd(A, U, Sigma, VT):
    A_reconstructed = np.dot(U, np.dot(Sigma, VT))
    return np.array_equal(A, A_reconstructed)

def main():
    print("Enter the matrix:")
    num_rows, num_cols = row_column_input()
    A = input_matrix(num_rows, num_cols)

    if not is_svd_possible(A):
        return

    try:
        U, Sigma, VT = svd_decomposition(A)
        print("U:\n", U)
        print("Sigma:\n", Sigma)
        print("V^T:\n", VT)

        if verify_svd(A, U, Sigma, VT):
            print("SVD verified successfully: A = U Σ V^T")
        else:
            print("SVD verification failed.")
    except Exception as e:
        print("SVD could not be performed:", str(e))

if __name__ == "__main__":
    main()
