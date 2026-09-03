#Time Complexity: O(n*n)
#Space Complexity: O(1)
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        n = len(mat)
        total_sum = 0
        for i in range(n):
            for j in range(n):
            #adding primrary diagonal elements
                if i == j:
                    total_sum += mat[i][j]
            #adding secondary diagonal_elements
                if i+j == n-1 and i != j:
                    total_sum += mat[i][j]

       
        
        return total_sum





        