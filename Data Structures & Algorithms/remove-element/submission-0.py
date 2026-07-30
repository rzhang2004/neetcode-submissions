class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0 # index in which to insert proper vals
        r = 0 # index for searching for proper vals

        while r < len(nums):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
            r += 1
        
        return l