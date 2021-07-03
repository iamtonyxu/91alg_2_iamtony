from typing import List
'''
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix
示例 1：
输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]

示例 2：
输入：n = 1
输出：[[1]]
'''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # simulation method
        # init matrix
        mat = [[0 for _ in range(n)] for _ in range(n)]
        # board of the block [l, t, r, b] = [0, n-1, 0, n-1]
        l, r, t, b = 0, n-1, 0, n-1
        num, target = 1, n ** 2
        while num <= target:
            # left -> right
            for i in range(l, r+1, 1):
                mat[t][i] = num
                num += 1
            t += 1
            # top -> bottom
            for i in range(t, b+1, 1):
                mat[i][r] = num
                num += 1
            r -= 1
            # right -> left
            for i in range(r, l-1, -1):
                mat[b][i] = num
                num += 1
            b -= 1
            # bottom -> top
            for i in range(b, t-1, -1):
                mat[i][l] = num
                num += 1
            l += 1
        return mat

if __name__ == "__main__":
    obj = Solution()
    for n in range(1, 10):
        matrix = obj.generateMatrix(n)
        print(matrix)