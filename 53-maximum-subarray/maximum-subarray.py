class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Approach:
        - Use Kadane’s Algorithm (Dynamic Programming).
        - Maintain a running sum of the current subarray.
        - Reset the sum if it becomes negative, and update the maximum sum at each step."""

        maxSub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
               curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)

        return maxSub