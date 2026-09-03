class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        n = len(mat)
        total_sum = 0
        for i in range(n):
            #adding primrary diagonal elements
            total_sum += mat[i][i]
            #adding secondary diagonal_elements
            total_sum += mat[i][n - 1 - i]

        if n % 2 != 0:
            total_sum = total_sum - mat[n//2][n//2]
        
        return total_sum





        