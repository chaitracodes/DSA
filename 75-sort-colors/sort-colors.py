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

