

def alternate_rectangle(r, c):

    if r == 0 or c == 0:
        return []

    matrix = [ [None] * c for _ in range(r) ]

    i, j, k, l = 0, len(matrix[0]) -1, len(matrix) -1, 0
    curr = 'X'

    while i <= k and l <= j:
        for right in range(l, j+1):
            matrix[i][right] = curr
        i += 1
        
        for down in range(i, k+1):
            matrix[down][j] = curr
        j -= 1

        if i > k:
            break           
        
        for left in range(j, l-1, -1):
            matrix[k][left] = curr
        k -= 1
        
        if l > j:
            break            
        
        for top in range(k, i-1, -1):
            matrix[top][l] = curr
        l += 1

        curr = 'X' if curr == '0' else '0'
                   
    return matrix


print(alternate_rectangle(1, 0))