class Solution:
    def isHappy(self, n: int) -> bool:
        
        visited = set()

        while n not in visited:
            visited.add(n)
            temp = str(n)
            n = 0
            for i in range(len(temp)):
                n += int(temp[i])**2
            
            if n == 1:
                return True
        
        return False