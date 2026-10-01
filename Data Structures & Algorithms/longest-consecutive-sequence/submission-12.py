class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = set(nums)
        checked = set()
        best = 0

        for i in nums:
            if i in checked or i-1 in n:
                continue
            curr = i
            curr_len = 1
            while curr not in checked and curr in n:
                best = max(best, curr_len)
                checked.add(curr)
                curr += 1
                curr_len += 1
        
        return best
        