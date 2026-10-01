class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # find row
        l = 0
        r = len(matrix) - 1

        while l <= r:
            mid = (l+r)//2

            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][-1] < target:
                l = mid + 1
            else:
                break

        # find idx
        lst = matrix[mid]
        l = 0
        r = len(lst) - 1
        while l <= r:
            mid = (l+r)//2

            if lst[mid] == target:
                return True
            elif lst[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False