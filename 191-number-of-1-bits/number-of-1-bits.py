class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n > 0:
            bit = n%2
            if bit != 0:
                result += 1
            n = n//2
        return result
                
        