'''
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、1 和 2 分别表示红色、白色和蓝色。

示例:
输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]
输入：nums = [2,0,1]
输出：[0,1,2]
输入：nums = [0]
输出：[0]
输入：nums = [1]
输出：[1]
'''

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        #1. 遍历数组，将如果当前元素为红色，
        """
        if len(nums) <= 1: return
        RED, WHITE, BLUE = 0, 1, 2
        # cur points to current node; p1 points to the end of 0s, p2 points to the start of 2s
        cur, p1, p2 = 0, 0, len(nums) - 1
        while cur <= p2:
            if nums[cur] == RED:
                nums[cur], nums[p1] = nums[p1], nums[cur]
                p1 += 1
                cur += 1
            elif nums[cur] == BLUE:
                nums[cur], nums[p2] = nums[p2], nums[cur]
                p2 -= 1
            else:
                cur += 1

if __name__ == "__main__":
    mySolution = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    mySolution.sortColors(nums)
    print(nums)

    nums = [2, 1, 0, 0, 2, 1, 1, 0, 0]
    mySolution.sortColors(nums)
    print(nums)

    nums = [1]
    mySolution.sortColors(nums)
    print(nums)