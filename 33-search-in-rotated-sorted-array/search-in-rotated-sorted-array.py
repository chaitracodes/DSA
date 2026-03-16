"""There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity."""

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

             
