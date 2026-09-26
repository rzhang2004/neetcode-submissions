import numpy as np

c = np.sqrt(5)

def fib(n):
    return int((1/c)*(((1+c)/2)**n - ((1-c)/2)**n))

class Solution:
    def climbStairs(self, n: int) -> int:
        return fib(n+1)