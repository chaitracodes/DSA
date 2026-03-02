class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        """Approach:
        - Go through the array and keep track of two values:
        - 1) the maximum product ending at the current position
        - 2) the minimum product ending at the current position
        - This is needed because a negative number can turn a small (negative) product
          into a large positive one.
        - Use a temporary variable so the old maximum is not lost while updating values.
        - Keep updating the overall maximum product."""

        result = max(nums)
        cur_max , cur_min = 1,1

        for n in nums:
            if n == 0:
                cur_max, cur_min = 1,1
            temp = cur_max * n
            cur_max = max(cur_max * n , cur_min * n, n)
            cur_min = min(temp , cur_min * n, n)
            result = max(result,cur_max)
        return result

