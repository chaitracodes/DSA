class Solution:
    def climbStairs(self, n: int) -> int:
        """Approach
        # At each step, we can reach it from the previous 1 or 2 steps.
        # This forms a recurrence relation similar to Fibonacci: f(n) = f(n-1) + f(n-2).
        # We optimize space by only storing the last two computed values instead of a full DP array.
        # Iterate up to n and return the final computed number of ways."""
        one, two=1, 1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one
        