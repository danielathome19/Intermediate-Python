"""
Description:
Read a 5 X 5 two-dimensional array (matrix) from an external data file.
The data is stored in rows.

Print the original array and its transpose with appropriate labels.

The transpose of a matrix is a new matrix formed by swapping the 
original matrix's rows and columns (i.e., The first row of the 
original matrix becomes the first column of the new matrix, the 
second row becomes the second column, and so on.)

Sample output:
Original Matrix
	45	67	89	12	-3	
	-3	-6	-7	-4	-9
	96	81	-8	52	12	
	14	-7	72	29	-1	
	19	43	28	63	87
	
Transpose
	45	-3	96	14	19
	67	-6	81	-7	43
	89	-7	-8	72	28
	12	-4	52	29	63
	-3	-9	12	-1	87
"""


def print_matrix(matrix: list[list[int]]) -> None:
    for row in matrix:
        print(' '.join(str(x) for x in row))
    pass


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    transposed = []
    for r in range(len(matrix)):         # len(matrix) tells us # of rows
        row = []
        for c in range(len(matrix[r])):  # len(matrix[row]) tells us # of cols in the row
            row.append(matrix[c][r])
        transposed.append(row)
    return transposed


def main():
    mat = []

    try:
        with open('lecture4/transpose.txt') as f:
            for line in f:
                row = [int(x) for x in line.split(' ')]
                mat.append(row)
    except FileNotFoundError:
        print("Error: File not found.")
        return

    mat_T = transpose(mat)

    print("Original: ")
    print_matrix(mat)

    print("\nTranspose: ")
    print_matrix(mat_T)
	
    pass


if __name__ == "__main__":
    main()
