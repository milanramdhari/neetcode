class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # transpose it and rever each row

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i < j:
                    # perform swap
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i] 
                    matrix[j][i] = temp

        def reverse(arr):
            left = 0
            right = len(matrix) - 1
            while left < right:
                temp = arr[left]
                arr[left] = arr[right]
                arr[right] = temp
                left += 1
                right -= 1
        
        for i in range(len(matrix)):
            reverse(matrix[i])
        

        