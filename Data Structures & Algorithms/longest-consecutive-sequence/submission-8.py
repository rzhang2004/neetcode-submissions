class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        already_checked = set()

        longest = 0
        for n in nums:
            if n in already_checked:
                continue
            
            curr_streak = 0
            curr = n
            while curr in num_set:
                already_checked.add(curr)
                curr += 1
                curr_streak += 1
            
            longest = max(longest, curr_streak)
        
        return longest
            