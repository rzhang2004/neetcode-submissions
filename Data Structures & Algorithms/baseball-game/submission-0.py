class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []

        for o in operations:
            if o == '+':
                s.append(s[-1] + s[-2])
            elif o == 'D':
                s.append(2*s[-1])
            elif o == 'C':
                s.pop()
            else:
                s.append(int(o))
        
        return sum(s)