class Solution:
    def fib(self, n: int) -> int:
        """Approach
        - Computes the nth Fibonacci number using an iterative dynamic programming approach.
        - The Fibonacci sequence is defined as:
           f(0) = 0, f(1) = 1
           f(n) = f(n-1) + f(n-2) for n >= 2
        - This implementation uses two variables to store the previous two values
          and updates them iteratively to avoid extra space."""
        if n <= 1:
            return n

        one, two = 0, 1
        for i in range(2,n+1):
            temp = one + two
            one = two
            two = temp
        return two