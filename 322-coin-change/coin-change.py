class Solution:
    """
    Approach
    - Use DP where dp[a] stores the minimum coins to make amount a.
    - Initialize dp[0] = 0 and others as infinity.
    - For each amount, try every coin and update dp[a] = min(dp[a], 1 + dp[a - c]).
    -Return dp[amount] if possible, else -1."""
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1+dp[a-c])
        return dp[amount] if dp[amount] != float('inf') else -1

        
"""
Use DP where dp[a] stores the minimum coins to make amount a.
Initialize dp[0] = 0 and others as infinity.
For each amount, try every coin and update dp[a] = min(dp[a], 1 + dp[a - c]).
Return dp[amount] if possible, else -1.
"""

        