def fib(n):
    a = b = 1
    for i in range(n-1):
        temp = a + b
        a = b
        b = temp
    return b

class Solution:
    def climbStairs(self, n: int) -> int:
        return fib(n)