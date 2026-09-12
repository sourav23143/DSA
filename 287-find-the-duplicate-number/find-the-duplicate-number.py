#Fast and Slow Pointer

#Time Complexity: O(n)
#Space Complexity: O(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        #Part 1: Finding the meeting point of the two pointer [slow and fast]
        while True:
            #one step at a time
            slow = nums[slow]
            #two step a time
            fast = nums[nums[fast]]
            if slow == fast:
                break
        #Part 2: Find the starting point/entrance of the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow] #one step
            fast = nums[fast] #one step
        return fast   



        

        