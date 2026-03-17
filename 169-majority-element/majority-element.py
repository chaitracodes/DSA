class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """Approach:
        - Use Boyer-Moore Voting Algorithm.
        - Maintain a candidate and a count.
        - If count becomes 0, select a new candidate.
        - Increase count when the number matches candidate, otherwise decrease it.
        - The final candidate is the majority element."""
        count = 0
        candidate = None

        for n in nums:
            if count == 0:
                candidate = n
            if candidate == n:
                count += 1
            else:
                count -= 1
        return candidate
        