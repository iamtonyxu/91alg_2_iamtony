from typing import List

class Solution:
	'''
	# Timeout Issue
	def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
		ans = 0
		incrSatisfied = 0
		coolTime = 0
		for i in range(len(customers)):
			tmp = 0
			max_index = i + X if i + X < len(customers) else len(customers)
			for j in range(i, max_index):
				if grumpy[j] == 1:
					tmp += customers[j]
			if tmp > incrSatisfied:
				incrSatisfied = tmp
				coolTime = i
		for i in range(len(customers)):
			if grumpy[i] == 0 or (i >= coolTime and i < coolTime + X):
				ans += customers[i]
		return ans
		'''

	def maxSatisfied_v2(self, customers: List[int], grumpy: List[int], X: int) -> int:
		grumpy = list(map(lambda x, y : x * y, customers, grumpy))
		maxGrumpSize, termGrumpSize = float("-inf"), 0
		for i in range(len(grumpy)):
			termGrumpSize += grumpy[i] if i < X else (grumpy[i] - grumpy[i - X])
			maxGrumpSize = max(maxGrumpSize, termGrumpSize)
		return sum(customers) - sum(grumpy) + maxGrumpSize

if __name__ == "__main__":
	customers = [1, 0, 1, 2, 1, 1, 7, 5]
	grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
	X = 3
	solution = Solution()
	print(solution.maxSatisfied_v2(customers, grumpy, X))
