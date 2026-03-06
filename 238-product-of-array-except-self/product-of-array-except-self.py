class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n

        # left products
        left = 1
        for i in range(n):
            res[i] = left
            left *= nums[i]

        # right products
        right = 1
        for i in range(n-1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res