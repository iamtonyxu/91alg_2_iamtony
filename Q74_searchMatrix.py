from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ## binary search
        start, end = 0, len(matrix) * len(matrix[0])
        while start <= end:
            mid = start + (end - start)//2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False

if __name__ == "__main__":
    matrix1 = [[1,3,5,7], [10,11,16,20], [23,30,34,60]]
    solution = Solution()
    print(solution.searchMatrix(matrix1, 25))
