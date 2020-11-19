from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return None
        hashTable = {}
        for i in range(0, len(nums)):
            if target - nums[i] in hashTable:
                return [hashTable[target - nums[i]], i]
            else:
                hashTable[nums[i]] = i
