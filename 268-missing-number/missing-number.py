class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        n = len(nums)
        for i in range(0, n+1):
            xor = xor ^ i
        for i in nums:
            xor = xor ^ i
        return xor