class Solution:
    def findMin(self, nums: List[int]) -> int:
        """# Approach:
        - Use binary search on the rotated sorted array.
        - If the current segment is sorted, nums[l] is the minimum.
        - Otherwise move towards the unsorted half to find the pivot."""
        res = nums[0]
        l,r = 0, len(nums) - 1
        
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res,nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        return res

        