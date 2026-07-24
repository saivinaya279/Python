def build_prefix_sum(arr):
    n = len(arr)
    prefix = [0] * (n + 1)   

    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]

    return prefix


def range_sum(prefix, left, right):
    
    return prefix[right + 1] - prefix[left]



arr = [2, 4, 1, 5, 3]
prefix = build_prefix_sum(arr)
print(range_sum(prefix, 1, 3))   
def build_2d_prefix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            prefix[i][j] = (matrix[i-1][j-1]
                             + prefix[i-1][j]
                             + prefix[i][j-1]
                             - prefix[i-1][j-1])
    return prefix


def range_sum_2d(prefix, r1, c1, r2, c2):
    return (prefix[r2+1][c2+1]
            - prefix[r1][c2+1]
            - prefix[r2+1][c1]
            + prefix[r1][c1])


matrix = [[1,2,3],[4,5,6],[7,8,9]]
prefix = build_2d_prefix(matrix)
print(range_sum_2d(prefix, 1, 1, 2, 2))   