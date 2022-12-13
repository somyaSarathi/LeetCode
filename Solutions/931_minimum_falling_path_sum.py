class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        N = len(matrix)

        if N == 1:
            return matrix[0][0]

        for i in range(N-2, -1, -1):
            for j in range(N):
                # col = 0
                if j == 0:
                    matrix[i][j] = min( matrix[i][j] + matrix[i+1][j], matrix[i][j] + matrix[i+1][j+1] )

                # col = N-1
                elif j == N-1:
                    matrix[i][j] = min( matrix[i][j] + matrix[i+1][j-1], matrix[i][j] + matrix[i+1][j] )

                else:
                    matrix[i][j] = min( matrix[i][j] + matrix[i+1][j-1], matrix[i][j] + matrix[i+1][j], matrix[i][j] + matrix[i+1][j+1] )

            # to save memory
            del matrix[i+1]

        return min(matrix[0])