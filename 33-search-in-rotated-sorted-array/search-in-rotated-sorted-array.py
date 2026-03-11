class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """ Approach:
        - Use binary search since the array was originally sorted but then rotated.-
        - At any step, one half of the array must be sorted.
        - Check whether the left half or the right half is sorted.
        - If the target lies within the sorted half, search there.
        - Otherwise, search in the other half.
        - Continue until the target is found or the search space becomes empty."""
        l = 0
        r = len(nums)-1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            # left half sorted    
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # right sorted array
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1

             