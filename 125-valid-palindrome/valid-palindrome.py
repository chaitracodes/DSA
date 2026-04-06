class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Approach: Two Pointers + Filtering
    - Use two pointers (left and right) starting from both ends of the string.
    - Skip non-alphanumeric characters using a helper function.
    - Compare characters in a case-insensitive manner.
    - If mismatch occurs, return False.
    - Move pointers inward and continue until they meet."""
        l, r=0, len(s)-1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l+1, r-1
        return True

    def alphaNum(self,c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
        