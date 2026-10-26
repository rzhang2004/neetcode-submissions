class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        checked = set()
        numset = set(nums)
        best = 0

        for n in nums:
            if n-1 in numset or n in checked:
                continue
            
            curr = 0
            while n in numset:
                checked.add(n)
                n += 1
                curr += 1
            
            best = max(curr, best)
        
        return best
