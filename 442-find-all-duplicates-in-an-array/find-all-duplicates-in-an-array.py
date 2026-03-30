
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """Approach:
        - Find all elements that appear twice using index marking.
        - Treat each value as an index (value - 1).
        - Traverse the array and mark visited indices by negating values.
        - If an index is already negative, the number is a duplicate."""
        res = []
        for n in nums:
            n = abs(n)
            if nums[n-1] < 0:
                res.append(n)
            nums[n-1] = -nums[n-1]

        return res
        
