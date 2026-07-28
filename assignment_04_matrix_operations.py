# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def transpose_matrix(matrix):
    # Get the number of rows and columns in the original matrix
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    # Create a new matrix for the transpose with swapped dimensions
    transposed = [[0] * rows for _ in range(cols)]

    # Fill the transposed matrix
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
            def add_matrices(matrix_a, matrix_b):
                # Get the number of rows and columns (assumed to be the same for both matrices)
                rows = len(matrix_a)
                cols = len(matrix_a[0]) if rows > 0 else 0

                # Create a new matrix for the sum
                result = [[0] * cols for _ in range(rows)]

                # Compute the element-wise sum
                for i in range(rows):
                    for j in range(cols):
                        result[i][j] = matrix_a[i][j] + matrix_b[i][j]
                        def multiply_matrices(matrix_a, matrix_b):
                            # Get dimensions
                            rows_a = len(matrix_a)
                            cols_a = len(matrix_a[0]) if rows_a > 0 else 0
                            rows_b = len(matrix_b)
                            cols_b = len(matrix_b[0]) if rows_b > 0 else 0

                            # Check if multiplication is possible (cols of A == rows of B)
                            if cols_a != rows_b:
                                raise ValueError("Number of columns in A must equal number of rows in B.")

                            # Create a new matrix for the product with dimensions rows_a x cols_b
                            result = [[0] * cols_b for _ in range(rows_a)]

                            # Compute the product
                            for i in range(rows_a):
                                for j in range(cols_b):
                                    for k in range(cols_a):  # or range(rows_b), since cols_a == rows_b
                                        result[i][j] += matrix_a[i][k] * matrix_b[k][j]
                                        return result
                                        def main():
                                            # Example usage of the functions
                                            # Part A: Transpose a matrix
                                            print("Part A: Transpose a Matrix")
                                            rows = int(input("Enter number of rows: "))
                                            cols = int(input("Enter number of columns: "))
                                            matrix = []
                                            for i in range(rows):
                                                row = list(map(int, input(f"Enter row {i + 1}: ").split()))
                                                matrix.append(row)
                                            transposed = transpose_matrix(matrix)
                                            print("Original Matrix:")
                                            for row in matrix:
                                                print(" ".join(map(str, row)))
                                            print("Transposed Matrix:")
                                            for row in transposed:
                                                print(" ".join(map(str, row)))
                                                if __name__ == "__main__":
                                                    main()
                                                    