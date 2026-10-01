class Solution:
    def trap(self, height: List[int]) -> int:
        # generate highest to left
        l_arr = []
        for i in range(len(height)):
            if not l_arr:
                l_arr.append(0)
            else:
                l_arr.append(max(l_arr[-1], height[i-1]))

        r_arr = []
        r = len(height) - 1
        while r >= 0:
            if not r_arr:
                #print(r)
                r_arr.append(0)
            else:
                #print(r)
                r_arr.append(max(r_arr[-1], height[r+1]))
            r -= 1
        
        r_arr = r_arr[::-1]

        total = 0
        for i in range(len(height)):
            total += max(0, min(l_arr[i], r_arr[i]) - height[i])
        
        return total
