class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # prefix
        l = 0
        prefix_arr = []
        while l < len(nums):
            if prefix_arr:
                prefix_arr.append(prefix_arr[-1] * nums[l-1])
            else:
                prefix_arr.append(1)
            l += 1

        # suffix
        r = len(nums) - 1
        suffix_arr = []
        while r >= 0:
            if suffix_arr:
                suffix_arr.append(suffix_arr[-1] * nums[r+1])
            else:
                suffix_arr.append(1)
            r -= 1
        
        suffix_arr = suffix_arr[::-1]
        
        return [prefix_arr[i] * suffix_arr[i] for i in range(len(prefix_arr))]