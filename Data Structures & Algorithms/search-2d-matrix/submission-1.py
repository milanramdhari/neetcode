class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if matrix[0] is None:
            return False

        # binary search 
        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        while (left <= right):
            mid = (left + right) // 2
            x = mid // len(matrix[0])
            y = mid % len(matrix[0])

            if matrix[x][y] == target:
                return True
            
            if matrix[x][y] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False


        