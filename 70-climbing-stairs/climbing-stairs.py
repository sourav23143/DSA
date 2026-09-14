class Solution:
    def climbStairs(self, n: int) -> int:
        # if n<=3 :
        #     return n
        # else:
        #     return self.climbStairs(n-1) + self.climbStairs(n-2)
        # RECURSION WILL NOT WORK AND GIVE TIME  LIMIT EXCEEDED ERROR

        #Interative approch>
        first = 1
        second = 2
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            for i in range(3, n+1):
                third = first + second
                first = second
                second = third
            return second
        