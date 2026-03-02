"""Given a string s, find the length of the longest substring without duplicate characters."""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      """ Approach:
      - Use a sliding window with two pointers.
      - Store the last index of each character using a hashmap.
      - Move the right pointer to expand the window.
      - If a character repeats inside the window, jump the left pointer
      - to one position after its previous occurrence.
      - Update the maximum window length at each step. """
        mp = {}
        left = 0
        res = 0

        for right, ch in enumerate(s):
            if ch in mp and mp[ch] >= left:
                left = mp[ch] + 1

            mp[ch]=right
            res = max(res, right - left + 1)
        return res
