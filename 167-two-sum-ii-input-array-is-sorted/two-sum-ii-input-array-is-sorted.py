class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """ Approach:
        - Since the array is sorted, use two pointers.
        - Start one pointer at the beginning (l) and the other at the end (r).
        - Compute the sum of numbers[l] + numbers[r].
        - If the sum is greater than the target, move the right pointer left to decrease the sum.
        - If the sum is smaller than the target, move the left pointer right to increase the sum.
        - If the sum equals the target, return the indices (1-indexed)."""
        l , r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return[l + 1 , r + 1]
        return[]

