class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        used = {}
        best = 0
        majority = 0

        while r < len(s):
            used[s[r]] = used.get(s[r], 0) + 1
            majority = max(used[s[r]], majority)
           # print(f'Majority: {majority} | Best: {best} | r: {r} | l: {l}')
            if majority + k >= r - l + 1:
                best = r - l + 1
            else:
                used[s[l]] -= 1
                l += 1
            r += 1
        
        return best