class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        best = 0
        used = {}
        while r < len(s):
            if s[r] in used:
                used.pop(s[l])
                l += 1
            else:
                best = max(r - l + 1, best)
                used[s[r]] = r
                r += 1

        return best
