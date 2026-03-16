class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """ Approach:
        - Use a hash set for O(1) lookup.
        - A number starts a sequence if n-1 is not in the set.
        - Expand the sequence forward and count its length.
        - Track the maximum sequence length."""

    # nums.sort() gives time complexity O(n log n)
        num_set = set(nums) # as set takes O(1) constant time to lookup, no matter the input sixe
        longest = 0

        for n in num_set:
            if (n - 1) not in num_set :
                length = 1
                while (n + length) in num_set:
                    length += 1
                longest = max(length , longest)
        return longest


        