"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.class Solution:"""

    def productExceptSelf(self, nums):
        """ Approach:
        - Instead of using division, compute the product of elements to the left
        and to the right of each index.
        - First pass: store the product of all elements before the current index.
        - Second pass: traverse from the right while maintaining a running right product
        - and multiply it with the stored left product.
        - This gives the product of all elements except the current one."""
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
