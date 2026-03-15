"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct."""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """ Approach:
        - Use a hashmap to track numbers already seen.
        - Traverse the array and check if the current number exists in the hashmap.
        - If it does, a duplicate is found.
        - Otherwise store the number in the hashmap."""
        mp = {}

        for num in nums:
            if num in mp:
                return True
            mp[num] = 1
            
        return False
