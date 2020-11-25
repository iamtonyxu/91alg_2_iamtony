from typing import List

class Solution:
	def searchInsert(self, nums: List[int], target: int) -> int:
		start, end = 0, len(nums)-1
		while start <= end:
			#mid = (start + end)//2
			mid = start + (end - start) // 2
			if nums[mid] == target:
				return mid
			elif nums[mid] < target:
				start = mid + 1
			else:
				end = mid - 1
		return start

	def searchInsert_v2(self, nums: List[int], target: int) -> int:

if __name__ == "__main__":
	nums = [1, 3, 5, 6]
	solution = Solution()
	print(solution.searchInsert(nums, 5))
	print(solution.searchInsert(nums, 2))
	print(solution.searchInsert(nums, 7))
	print(solution.searchInsert(nums, 0))
	nums = [1, 3]
	print(solution.searchInsert(nums, 4))