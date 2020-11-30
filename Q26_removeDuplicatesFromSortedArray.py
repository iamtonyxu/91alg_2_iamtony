from typing import List


class Solution(object):
	def removeDuplicates(self, nums: List[int]) -> int:
		if not nums: return 0
		wr_index = 0
		for rd_index in range(len(nums)):
			if nums[rd_index] != nums[wr_index]:
				wr_index += 1
				nums[wr_index] = nums[rd_index]
		return wr_index + 1


if __name__ == "__main__":
	solution = Solution()
	nums1 = [0, 0, 0, 1, 1, 2, 2, 3, 4, 4, 5, 5]
	# nums1 = [0, 0, 0]
	for i in range(0, solution.removeDuplicates(nums1)):
		print(nums1[i])
