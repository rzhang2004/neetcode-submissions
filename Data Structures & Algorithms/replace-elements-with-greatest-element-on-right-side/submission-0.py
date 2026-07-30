class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max = -1
        r = len(arr) - 1
        r_max = []
        while r >= 0:
            r_max.append(curr_max)
            curr_max = max(curr_max, arr[r])
            r -= 1
        
        return r_max[::-1]

