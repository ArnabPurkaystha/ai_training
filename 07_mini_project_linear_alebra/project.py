import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations

def input_vectors():
    """Input vectors interactively as numbers separated by spaces."""
    print("Enter vectors in 2D or 3D space as space-separated numbers (e.g., '1 2' or '1 2 3'). Enter 'done' to finish:")
    vectors = []
    dim = None
    while True:
        inp = input(f"Vector {len(vectors) + 1}: ")
        if inp.lower() == "done":
            break
        try:
            vector = list(map(int, inp.split()))
            if dim is None:
                dim = len(vector)
            if len(vector) != dim:
                print(f"Please enter a vector of dimension {dim}.")
            else:
                vectors.append(vector)
        except ValueError:
            print("Invalid input. Please enter space-separated integers.")
    return np.array(vectors), dim

def check_independence(vectors):
    """Check linear dependence/independence."""
    if len(vectors) == 0:
        return
    print("\nChecking linear independence...")
    matrix = np.stack(vectors, axis=1)
    rank = np.linalg.matrix_rank(matrix)
    print(f"The rank of the matrix is: {rank}")
    if rank == len(vectors):
        print("The vectors are linearly independent.")
    else:
        print("The vectors are linearly dependent.")

def compute_span(vectors):
    """Visualize the span of vectors in 2D."""
    if len(vectors) == 0 or len(vectors[0]) != 2:
        print("Span visualization is only available for 2D vectors.")
        return
    print("\nVisualizing the span of the vectors...")
    plt.figure()
    for vec in vectors:
        plt.quiver(0, 0, vec[0], vec[1], angles='xy', scale_units='xy', scale=1, color='r', alpha=0.5)
    # Generate the span
    x = np.linspace(-10, 10, 100)
    for combo in combinations(vectors, 2):
        a, b = combo
        for t1 in x:
            for t2 in x:
                point = t1 * a + t2 * b
                plt.plot(point[0], point[1], 'bo', markersize=0.5, alpha=0.1)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.grid()
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.title("Span of Vectors")
    plt.show()

def find_basis(vectors):
    """Find a basis for the span."""
    if len(vectors) == 0:
        return
    print("\nFinding the basis for the span...")
    matrix = np.stack(vectors, axis=1)
    rank = np.linalg.matrix_rank(matrix)
    u, s, vh = np.linalg.svd(matrix)
    basis_vectors = vh[:rank].T
    print(f"Basis vectors:\n{basis_vectors}")
    return basis_vectors

def linear_combination(vectors):
    """Find coefficients to represent a given vector as a linear combination."""
    if len(vectors) == 0:
        return
    try:
        resultant_vector = np.array(eval(input("\nEnter the resultant vector to represent: ")), dtype=float)
        coefficients = np.linalg.lstsq(np.stack(vectors).T, resultant_vector, rcond=None)[0]
        print(f"Coefficients to represent the resultant vector:\n{coefficients}")
        print(f"Linear combination: ", 
              " + ".join([f"({coeff}) * {vec}" for coeff, vec in zip(coefficients, vectors)]))
    except Exception as e:
        print(f"Error: {e}\nThe vector cannot be represented as a linear combination of the given vectors.")

# Main program
if __name__ == "__main__":
    print("Welcome to the Vector Space and Linear Transformation Program!")
    vectors, dimension = input_vectors()
    if len(vectors) > 0:
        check_independence(vectors)
        if dimension == 2:
            compute_span(vectors)
        basis = find_basis(vectors)
        linear_combination(vectors)
    else:
        print("No vectors provided.")
