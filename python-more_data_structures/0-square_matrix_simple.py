def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    result_matrix = []
    
    # Iterate over each row in the input matrix
    for row in matrix:
        # Create a new row for the result matrix
        result_row = []
        
        # Iterate over each element in the current row and compute its square
        for element in row:
            squared_value = element ** 2
            result_row.append(squared_value)
        
        # Add the current row to the result matrix
        result_matrix.append(result_row)
    
    return result_matrix

# Test the function
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = square_matrix_simple(matrix)
print(result)
