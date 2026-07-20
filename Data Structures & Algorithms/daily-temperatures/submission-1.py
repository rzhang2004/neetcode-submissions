class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []

        out = [0] * len(temperatures)

        for i in range(len(temperatures)):
            
            if not stack:
                stack.append((temperatures[i], i))
            else:
                while stack and temperatures[i] > stack[-1][0]:
                    out[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
                stack.append((temperatures[i], i))
        
        return out