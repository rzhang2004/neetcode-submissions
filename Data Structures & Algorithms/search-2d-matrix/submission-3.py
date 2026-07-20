class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # find greatest row that is still smaller than target
        t = 0
        b = len(matrix) - 1
        row = 0

        while t <= b:
            mid = (t+b)//2

            if matrix[mid][0] > target:
                b = mid - 1
            elif matrix[mid][0] < target:
                row = max(row, mid)
                t = mid + 1
            else:
                return True

        # binary search that row
        l = 0
        r = len(matrix[row]) - 1

        while l <= r:
            mid = (l+r)//2

            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
        
        return False


