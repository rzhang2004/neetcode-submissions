class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # time = (target - position) / speed

        both = list(zip(position, speed))

        both.sort(reverse=True)

        times = [(target - position)/speed for position, speed in both]

        stack = []

        for t in times:
            if not stack:
                stack.append(t)
            elif t > stack[-1]:
                stack.append(t)
        
        return len(stack)



