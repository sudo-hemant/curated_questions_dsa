

def searchMatrix(matrix, target):
    
    if not len(matrix) or not len(matrix[0]):
        return False
    
    if target < matrix[0][0] or matrix[-1][-1] < target:
        return False
    
    return row_search(matrix, target)
    

def row_search(matrix, target):
    
    low, high = 0, len(matrix) - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if matrix[mid][0] <= target and target <= matrix[mid][len(matrix[0]) - 1]:
            return column_search(mid, matrix, target)
        
        elif target < matrix[mid][0]: 
            high = mid - 1
            
        elif matrix[mid][0] < target:
            low = mid + 1
    
    return False


def column_search(row, matrix, target):
    
    low, high = 0, len(matrix[0]) - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if matrix[row][mid] == target:
            return True
        
        elif target < matrix[row][mid]:
            high = mid - 1
        
        elif matrix[row][mid] < target:
            low = mid + 1
    
    return False


# --------------------------------------------------------


# NOTE: 

# n * m matrix convert to an array => matrix[x][y] => a[x * m + y]
# an array convert to n * m matrix => a[x] =>matrix[x / m][x % m];

# NOT DONE MYSELF

def searchMatrix_2( matrix, target):
    if not matrix or target is None:
        return False

    rows, cols = len(matrix), len(matrix[0])
    low, high = 0, rows * cols - 1
    
    while low <= high:
        mid = (low + high) / 2
        num = matrix[mid / cols][mid % cols]
    
        if num == target:
            return True
        elif num < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return False