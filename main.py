

matrixA = [
    [4, 3], 
    [5, 7],
    [8, 5],
    [2, 1]
]


matrixB = [
    [2, 7, 2], 
    [3, 5, 4]
]


# Get size of matrix
def get_row_column(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    return [rows, columns]

# Check if two matrices are able to be multiplied
def check_valid_matrix(matrixA, matrixB):
    size_matrixA = get_row_column(matrixA)
    size_matrixB = get_row_column(matrixB)
    if size_matrixA[1] == size_matrixB[0]:
        return True
    else: 
        return False

# Get the size of the resulting matrix when two matrices are multiplied
def get_size(matrixA, matrixB):
    sizeA = get_row_column(matrixA) 
    sizeB = get_row_column(matrixB)
    total_size = [sizeA[0], sizeB[1]]
    return total_size

# Make a empty matrix based on a given size
def make_empty_matrix(size):
    empty_matrix = []
    rows = size[0]
    columns = size[1]
    for i in range(0, rows):
        empty_matrix.append([])
        for n in range(0, columns):
            empty_matrix[i].append("e")
    return empty_matrix

# multiply each item in the two lists, add it to the total. So when [1, 4] and [5, 3] are given the result will be (1*5) + (4*3) = 17
def multiply_and_add(items1, items2):
    total = 0
    for i in range(0, len(items1)):
        total = total + (items1[i]*items2[i])
    return total

# Doesn't really mirror a matrix but kind of turns it 90 degrees, making the code for multiplying a little easier
def mirror_matrix(matrix):
    empty_list = []
    size = get_row_column(matrix)
    export_matrix = make_empty_matrix([size[1], size[0]])
    for it in range(0, len(matrix[0])):
        for n in matrix:
            empty_list.append(n[it])
    for it in range(0, len(export_matrix)):
        for n in range(0, len(export_matrix[it])):
            export_matrix[it][n] = empty_list.pop(0)
    return export_matrix

# Does what it says it does. Dumbs all the values in an empty list and then fills the new matrix with that list.
def multiply_matrix(matrixA, matrixB):
    raw_output_list = []
    if check_valid_matrix(matrixA, matrixB) == False:
        raise ValueError("These matrices don't have the right sizes")
    outcome_size = get_size(matrixA, matrixB)
    target_matrix = make_empty_matrix(outcome_size)
    mirror_matrixB = mirror_matrix(matrixB)
    for row in range(len(matrixA)):
        for column in range(len(matrixB[0])):
            to_insert = multiply_and_add(matrixA[row], mirror_matrixB[column])
            raw_output_list.append(to_insert)
    for row in range(len(target_matrix)):
        for column in range(len(target_matrix[0])):
            target_matrix[row][column] = raw_output_list.pop(0)
    return target_matrix


print(multiply_matrix(matrixA, matrixB))