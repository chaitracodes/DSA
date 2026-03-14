class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """ Approach:
        - Use two pointers to track the position of non-zero elements.
        - Traverse the array and whenever a non-zero element is found,
        - swap it with the element at the left pointer.
        - This moves all zeros to the end while maintaining order."""
        l = 0

        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        