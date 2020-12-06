from typing import List
from collections import deque

class Solution:
	## 暴力法：超出时间限制
	def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
		# 遍历数组nums,
		# 维护一个maxValueInWindow,如果正在访问的成员大于maxValueInWindow，则更新maxValueInWindow
		# 并将maxValueInWindow加入结果数组
		res, maxValueInWindow = [], float("-inf")
		if len(nums) < k:
			maxValueInWindow = max(nums)
			res.append(maxValueInWindow)
			return res
		for i in range(k, len(nums)+1):
				maxValueInWindow = max(nums[i-3:i])
				res.append(maxValueInWindow)
		return res

	## 双向队列
	# 处理前 k 个元素，初始化双向队列。
	# 遍历整个数组。在每一步 :
		# 清理双向队列 :
        # - 只保留当前滑动窗口中有的元素的索引
        # - 移除比当前元素小的所有元素，它们不可能是最大的
		# 将当前元素添加到双向队列中。
		# 将 deque[0] 添加到输出中。
		# 返回输出数组。
	def maxSlidingWindow_v2(self, nums: List[int], k: int) -> List[int]:
		# 基准情况
		if len(nums) <= k:
			return [max(nums)]
		elif k == 1:
			return nums

		def clean_deque(i: int):
			# 只保留当前滑动窗口中有的元素的索引
			if deq and deq[0] == i - k:
				deq.popleft()
			# 移除比当前元素小的所有元素，它们不可能是最大的
			while deq and nums[deq[-1]] < nums[i]:
				deq.pop()

		# 初始化deq和output
		deq, max_idx = deque(), 0
		for i in range(k):
			clean_deque(i)
			deq.append(i)
			# 计算max_idx
			if nums[i] > nums[max_idx]:
				max_idx = i
			output = [nums[max_idx]]
		# 遍历数组
		for i in range(k, len(nums)):
			clean_deque(i)
			deq.append(i)
			output.append(nums[deq[0]])
		# 返回结果
		return output



if __name__ == "__main__":
	#nums = [1, 3, -1, -3, 5, 3, 6, 7]
	nums = [1]
	k = 3
	solution = Solution()
	res = solution.maxSlidingWindow(nums, k)
	print("direct method")
	for n in res:
		print(n)

	res = solution.maxSlidingWindow_v2(nums, k)
	print("deque method")
	for n in res:
		print(n)
