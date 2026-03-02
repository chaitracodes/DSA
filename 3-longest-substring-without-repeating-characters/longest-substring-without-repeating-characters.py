class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        left = 0
        res = 0

        for right, ch in enumerate(s):
            if ch in mp and mp[ch] >= left:
                left = mp[ch] + 1

            mp[ch]=right
            res = max(res, right - left + 1)
        return res



        