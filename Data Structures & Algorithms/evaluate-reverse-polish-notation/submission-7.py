class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for t in tokens:
            
            if t not in {'+', '-', '*', '/'}:
                stack.append(int(t))
            else:
                if t == '+':
                    stack[-2] += stack[-1]
                elif t == '-':
                    stack[-2] -= stack[-1]
                elif t == '*':
                    stack[-2] *= stack[-1]
                else:
                    stack[-2] = int(stack[-2] / stack[-1])
                stack.pop()
        
        return stack[0]