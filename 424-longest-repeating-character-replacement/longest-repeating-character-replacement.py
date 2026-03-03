class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        l = 0
        maxf = 0
        res = 0

        for r in range(len(s)):
            mp[s[r]] = mp.get(s[r], 0) + 1
            maxf = max(maxf, mp[s[r]])

            if (r - l + 1) - maxf > k:
                mp[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res