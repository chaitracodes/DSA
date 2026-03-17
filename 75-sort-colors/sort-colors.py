"""Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function."""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0 , len(nums) - 1
        m = 0

        while m <= r:
            if nums[m] == 0:
                nums[m] , nums[l] = nums[l] , nums[m]
                l += 1
                m += 1
            elif nums[m] == 1:
                m += 1  
            else:
                nums[r] , nums[m] = nums[m] , nums[r] 
                r -= 1

