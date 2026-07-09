class Solution:
    def trap(self, height: List[int]) -> int:
        
        hleft = []
        hright = []

        # min(hleft[i], hright[i]) - height[i]

        l = 0
        while l < len(height):
            if not hleft:
                hleft.append(height[l])
            else:
                hleft.append(max(hleft[-1], height[l]))
            l += 1
        
        r = len(height) - 1
        while r >= 0:
            if not hright:
                hright.append(height[r])
            else:
                hright.append(max(hright[-1], height[r]))
            r -= 1
        
        hright = hright[::-1]

        tally = 0
        for i in range(len(height)):
            tally += max(min(hleft[i], hright[i]) - height[i], 0)
        
        return tally