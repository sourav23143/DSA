class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        count = {}
        nums.sort()
        for i in range(1, len(nums)+1):
            if nums[i-1] == nums[i]:
                return nums[i]

        

        