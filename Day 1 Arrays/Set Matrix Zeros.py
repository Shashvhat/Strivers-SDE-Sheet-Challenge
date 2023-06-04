class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n,m,v = len(matrix),len(matrix[0]),5864834364538436
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    for k in range(m):
                        if k==j or matrix[i][k] == 0:
                            continue
                        matrix[i][k] = v
                    for k in range(n):
                        if k==i or matrix[k][j] == 0:
                            continue
                        matrix[k][j] = v
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == v:
                        matrix[i][j] = 0
