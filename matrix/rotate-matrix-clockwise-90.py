
def rotate(matrix):
    
    for i, row in enumerate(matrix):
        for j, column in enumerate(row):
            if j >= i:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
    for i, row in enumerate(matrix):
        low, high = 0, len(row) - 1
        while low < high:
            matrix[i][low], matrix[i][high] = matrix[i][high], matrix[i][low]
            low, high = low+1, high-1
    