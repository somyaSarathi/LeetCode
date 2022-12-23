class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # base case
        if text1 == text2:
            return len(text1)

        mat = [ [ 0 for i in range( len(text2) + 1) ] for i in range( len(text1) + 1 ) ]

        for i in range( len(text1)-1, -1, -1 ):
            for j in range( len(text2)-1, -1, -1 ):
                
                if text1[i] == text2[j]:
                    mat[i][j] = 1 + mat[i+1][j+1]

                else:
                    mat[i][j] = max(mat[i+1][j], mat[i][j+1])
        
        return mat[0][0]
    