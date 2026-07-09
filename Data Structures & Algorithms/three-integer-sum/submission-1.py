class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # sort
        nums.sort()

        # two pointers + LEFT pointer
        l = 0

        if len(nums) < 3:
            return []

        sols = []

        while l < len(nums) - 2:

            r1 = l + 1
            r2 = len(nums) - 1

            while r1 < r2:
                if nums[r1] + nums[r2] + nums[l] == 0:
                    sols.append((nums[l], nums[r1], nums[r2]))
                    r1 += 1
                elif nums[r1] + nums[r2] + nums[l] > 0:
                    r2 -= 1
                else:
                    r1 += 1

            l += 1
        
        return list(set(sols))

