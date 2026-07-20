class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # bin search until l < r
        # then return l

        l = 0
        r = len(nums) - 1

        while nums[l] > nums[r]:
            mid = (l+r)//2
            print(l, r, mid)

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        return nums[l]