class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """ Approach:
        - Since the array is sorted, duplicates appear consecutively.
        - Use two pointers where r scans the array and 
        - l tracks the position for the next unique element.
        - When a new number is found, place it at position l."""
        l = 1
        
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l

        