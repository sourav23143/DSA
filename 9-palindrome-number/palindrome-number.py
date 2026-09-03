#Time Complexity:  O(n)
#Space Complexity: O(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        #1. typecasting: converted x from int type to str type
        x = str(x)
        #2. Comparision whether the original string and the reversed strings are same or not
        if x == x[::-1]:
            return True

        return False
        