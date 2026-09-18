class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_all = 0
        n = len(nums)
        for i in range(0, n+1):
            xor_all = xor_all ^ i
        for i in nums:
            xor_all = xor_all ^ i
        return xor_all